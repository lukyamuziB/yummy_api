from . import app
from . import api
from . import jwt_file
from .. models import User


@api.route('/categories')