from flask import Blueprint, render_template
# from flask_login import login_manager

login = Blueprint('login', __name__)

#mock
users = {'test': {'password': 'password'}}

@login.route("/")
def loginPage():
    return render_template("login.html")
