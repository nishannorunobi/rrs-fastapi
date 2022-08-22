# Install VSCODE python plugins 
IntelliSense (Pylance), Linting, Debugging (multi-threaded, remote), Jupyter Notebooks, code formatting, refactoring, unit tests

# Create a Virtual Environment with local version
python -m venv rrsenv

# Create a Virtual Environment with a specific version
F:\python\python3.7\python.exe -m venv rrsenv

# Enter into virtual environment
.\rrsenv\Scripts\activate

# Following Commands has been executed to run the project successfully
# Inside the porject directory
pip3 install -r requirements.txt

# to Exit from virualenv
deactivate

# To delete virtual environment, delete env directory
rm -rf rrsenv

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
http://127.0.0.1:8000/docs

