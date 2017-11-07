from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import config


db = SQLAlchemy()


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config['development'])
    config['development'].init_app(app)


    db.init_app(app)
    
    
    """Blue print registration"""
    from .api import api as api_blueprint
    app.register_blueprint(api_blueprint)

    from .auth import auth as auth_blueprint
    app.register_blueprint(api_blueprint, url_prefix = '/auth')


    return app
