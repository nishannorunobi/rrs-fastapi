# Following Commands has been executed to run the project successfully
sudo pip3 install pipenv
pipenv shell
pipenv install fastapi
pipenv install uvicorn
sudo pip3 install numpy

#To start app
uvicorn main:app --reload

#To deploy in gcp
python3 -V
virtualenv -V
virtualenv env
source env/bin/activate
pip install -r dependencies.txt

# test if the server is running
gunicorn -w 4 -k uvicorn.workers.UvicornWorker main:app

# create app engine
gcloud app create
gcloud app deply app.yml


# output
descriptor:                  [/home/nishancse/rrs-fastapi/app.yml]
source:                      [/home/nishancse/rrs-fastapi]
target project:              [resumerankingsystem]
target service:              [default]
target version:              [20210818t190234]
target url:                  [https://resumerankingsystem.el.r.appspot.com]
target service account:      [App Engine default service account]

