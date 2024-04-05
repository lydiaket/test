from flask import Blueprint, render_template # blueprint- a way to separate app so that views can be defined in multiple files
from flask_login import login_user, login_required, logout_user, current_user

views = Blueprint('views', __name__) 


@views.route('/') 
@login_required # cannot get to home page unless you log in
def home():
    return render_template("home.html")