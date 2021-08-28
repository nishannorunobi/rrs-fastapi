from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import pickle

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

pkl_file = open("./resources/resume_dict.pkl","rb")
resume_data_dict = pickle.load(pkl_file)
pkl_file.close()
resume_dict_key_list=list(resume_data_dict.keys())
resume_dict_len = len(resume_dict_key_list)

#Write APIS
@app.get('/')
async def root():
    return {'hello' : 'world'}

#To access api doc
# {base-url}/docs

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
    total_pages = resume_dict_len / size
    if page > total_pages:
        return {}
    
    offset = page*size
    start_index = offset - size
    if start_index < 0:
        start_index = 0

    if offset > resume_dict_len:
        offset = resume_dict_len

    keys_to_extract = resume_dict_key_list[start_index : offset]

    paginated_resume_data_dict = {key: resume_data_dict[key] for key in keys_to_extract}
    return paginated_resume_data_dict