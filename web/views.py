from flask import Blueprint
from flask import render_template, redirect
views = Blueprint('views',__name__)
# @views.route('/')
# def home():
#     return render_template('index.html')

import subprocess

@views.route('/dashboard')
def dashboard():
    subprocess.Popen(["streamlit", "run", "/home/hiepd/softwareEngine/web_site/web/dashboard.py", "--server.port=8501"])
    return redirect('http://localhost:8501')