# Following Commands has been executed to run the project successfully
# Inside the porject directory
/usr/local/bin/python3.7 -m venv env
source env/bin/activate
pip3 install -r requirements.txt

# To start app
unicorn main:app --reload