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
