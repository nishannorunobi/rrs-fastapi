# Following Commands has been executed to run the project successfully
# Inside the porject directory
/usr/local/bin/python3.7 -m venv env
source env/bin/activate
pip3 install -r requirements.txt

# to Exit from virualenv
deactivate

# To start app
unicorn main:app --reload

# Create a Procfile for heroku to run the app with following commands
# You can run this command in your local machine as well
gunicorn -w 4 -k uvicorn.workers.UvicornWorker main:app

# Before final deployment
pip3 freeze > requirements.txt
