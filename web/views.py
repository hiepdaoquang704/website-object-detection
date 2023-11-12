from flask import Blueprint, Response
from flask import render_template, redirect
from flask import render_template, redirect, url_for
from flask_login import login_required, current_user


views = Blueprint('views',__name__)
@views.route('/')
def home():
    return render_template('index.html')
import subprocess
@views.route('/dashboard')
@login_required
def dashboard():
    if current_user.is_authenticated:
        subprocess.Popen(["streamlit", "run", "app.py", "--server.port=8502"])
        return Response(status=204)
    else:
        return redirect(url_for('auth.login'))
