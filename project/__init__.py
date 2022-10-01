'''
Fix:
# python -m pip install --upgrade pip
# python -m pip install --no-use-pep517 flask-bcrypt
'''
from flask import Flask


app = Flask(__name__)
app.config['SECRET_KEY'] = 'thisisfirstflaskapp'
app.config['UPLOAD_FOLDER'] = "static/data/"


from project import routes
