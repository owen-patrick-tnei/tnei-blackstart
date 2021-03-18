from flask import Blueprint, render_template

login = Blueprint('login', __name__)

@login.route("/")
def loginPage():
    return render_template("login.html")