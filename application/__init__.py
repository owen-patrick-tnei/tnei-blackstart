from flask import Flask
from flask import render_template


def init_app():
    """Initialize the core application."""
    app = Flask(__name__)
    # app.config.from_object('config.Config')

    with app.app_context():
        from . import routes
        from .dash.login import init_login
        app = init_login(app)
        from .dash.data import init_data
        app = init_data(app)


        return app