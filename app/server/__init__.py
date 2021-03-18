from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

from app.server.blueprints.login.login import login

db = SQLAlchemy()
login_manager = LoginManager()

def init_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    app.register_blueprint(login,url_prefix='/login')

    with app.app_context():
        # from .dash.login import init_login
        # app = init_login(app)
        from app.server.dash.data import init_data
        app = init_data(app)

        return app