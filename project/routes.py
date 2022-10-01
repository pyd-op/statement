import requests, os, random
from project import app
from datetime import date, time, datetime, timedelta
from flask import request
from flask import render_template
from flask import abort
from flask import send_from_directory
from flask import current_app

# ---------------------
# DevBox Implementation
# ---------------------

@app.route('/home', methods=['GET', 'POST'])
@app.route('/', methods=['GET', 'POST'])
def home():
   return render_template('home.html')

# ---------------------
# Helper Function
# ---------------------

@app.route("/download/<name>", methods=['GET', 'POST'])
def download(name):
    print("++")
    dir = os.path.join(current_app.root_path, app.config['UPLOAD_FOLDER'])
    print(dir)
    try:
        return send_from_directory(directory=dir, filename=name, as_attachment=True)
    except FileNotFoundError:
        abort(404)
