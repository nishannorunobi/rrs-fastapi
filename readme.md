# Install virtualenv packages in your local python environment
pip3 install virtualenv

# Install VSCODE python plugins 
IntelliSense (Pylance), Linting, Debugging (multi-threaded, remote), Jupyter Notebooks, code formatting, refactoring, unit tests

# Create a Virtual Environment with local version
virtualenv -m myenv

# Create a Virtual Environment with a specific version
virtualenv -p F:\python\python3.7\python.exe myenv

# Enter into virtual environment
source env/bin/activate

# Following Commands has been executed to run the project successfully
# Inside the porject directory
pip3 install -r requirements.txt

# to Exit from virualenv
deactivate

# To delete virtual environment, delete env directory
rm -rf env

# To start app
uvicorn main:app --reload

# Create a Procfile for heroku to run the app with following commands
# You can run this command in your local machine as well
gunicorn -w 4 -k uvicorn.workers.UvicornWorker main:app

# Before final deployment
pip3 freeze > requirements.txt


# to generate procfile to mention python version, so same version would be in heroku
pipenv lock


# Access swagger api
http://localhost:8080/docs