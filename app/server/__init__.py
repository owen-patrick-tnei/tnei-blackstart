from flask import Flask
from flask_login import LoginManager, login_required
from flask_sqlalchemy import SQLAlchemy

login_manager = LoginManager()
db = SQLAlchemy()
from app.server.models.User import User

from app.server.blueprints.login.login import login

def init_app():
    app = Flask(__name__)
    login_manager.init_app(app)
    db.init_app(app)


    app.config.from_pyfile('config.py')
    app.register_blueprint(login,url_prefix='/')

    with app.app_context():

        db.create_all()
        db.session.commit()
        user = User(password='password', email='test')
        db.session.add(user)
        db.session.commit()

        from app.server.dash.data import init_data
        app = init_data(app)

        from . import routes

        return app


#mock
users = {'test': {'password': 'password'}}

@login_manager.user_loader
def user_loader(user_id):
    # print(user_id)
    userDetails = User.query.get(user_id)
    # print(userDetails["password"])
    return userDetails






