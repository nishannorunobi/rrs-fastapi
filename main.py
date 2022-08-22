from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import pickle
from starlette.responses import FileResponse
from starlette.responses import StreamingResponse

import numpy

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

pkl_file = open("./resources/resume_list.pkl","rb")
resume_list = pickle.load(pkl_file)
pkl_file.close()
total_resume = len(resume_list)

#Write APIS
@app.get('/')
async def root():
    return {'hello' : 'world'}

@app.get('/resume-category')
async def root():
    pickle_in = open("./resources/resume_category.pkl","rb")
    doc_category = pickle.load(pickle_in)
    pickle_in.close()
    return doc_category

#Doc name list
@app.get('/download/{file_name}')
async def root(file_name: str):
    file_name = 'resume_sample.pdf'
    file_like = open('./resources/'+file_name, mode="rb")
    return StreamingResponse(file_like, media_type="application/pdf")
    #return FileResponse('./resources/'+file_name, media_type='application/octet-stream',filename=file_name)

#Doc name list
@app.get('/resume-names')
async def root():
    pickle_in = open("./resources/doc_name_list.pickle","rb")
    doc_name_list = pickle.load(pickle_in)
    pickle_in.close()
    return doc_name_list

#Overall rank score list
@app.get('/overall-ranks')
async def root():
    pickle_in = open("./resources/over_all_ranking_list.pickle","rb")
    over_all_ranking_list = pickle.load(pickle_in)
    pickle_in.close()
    return over_all_ranking_list

#API of experience of years ranking
@app.get('/experience-ranks')
async def root():
    pickle_in = open("./resources/years_of_experience_list.pickle","rb")
    years_of_experience_list = pickle.load(pickle_in)
    pickle_in.close()
    return years_of_experience_list

#API of experience of years ranking
@app.get('/requirement-matching-scores')
async def root():
    pickle_in = open("./resources/similarity_socre_list.pickle","rb")
    similarity_socre_list = pickle.load(pickle_in)
    pickle_in.close()
    return similarity_socre_list

@app.get('/get-paginated-data')
async def getPaginatedData(page: int = 1, size: int = 5):
    total_pages = total_resume / size
    if page > total_pages:
        return {}
    
    offset = page*size
    start_index = offset - size
    if start_index < 0:
        start_index = 0

    if offset > total_resume:
        offset = total_resume

    paginated_resume_list = resume_list[start_index : offset]
    return paginated_resume_list

import numpy as np;

@app.get('/get-chart-list')
async def getDesiredData(page: int = 1, size: int = 5):
    total_pages = total_resume / size
    if page > total_pages:
        return {}
    
    offset = page*size
    start_index = offset - size
    if start_index < 0:
        start_index = 0

    if offset > total_resume:
        offset = total_resume

    paginated_resume_list = resume_list[start_index : offset]
    
    empty_array = [['resumes','overall','similarity','years']];
    for obj in paginated_resume_list:
        arr = [[obj.get('doc_name'),obj.get('performance'),obj.get('similarity_score_1'),obj.get('years_of_experience')]];
        empty_array = empty_array + arr;
    return empty_array;