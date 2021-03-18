import flask
from flask import Blueprint, render_template, request
from flask_login import LoginManager, login_user
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from flask import current_app as app
from app.server import User

login = Blueprint('login', __name__)

login_manager = LoginManager()


@login.route("/",methods=['GET', 'POST'])
def loginPage():
    form = LoginForm(request.form)
    print("accessed page")

    if form.validate_on_submit():

        # Login and validate the user.
        # user should be an instance of your `User` class
        id = request.form.get('email')
        user = User.query.get(id)
        login_user(user)

        flask.flash('Logged in successfully.')
        print("logged in successfully")
        next = flask.request.args.get('next')
        return flask.redirect(next or flask.url_for('/dash/data/'))
    else:
        print("form did not validate")
    return flask.render_template('login.html',form=form)


class LoginForm(FlaskForm):
    username = StringField('email')
    password = PasswordField('password')

