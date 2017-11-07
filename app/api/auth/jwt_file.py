from models import User
from . import app
from flask_jwt import JWT, jwt_required

def verify():
    pass

def identity():
    pass

jwt = JWT(app, verify, identity)
