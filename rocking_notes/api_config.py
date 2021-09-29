from flask_jwt import JWT
from flask_jwt_extended import JWTManager
from flask_restful import Api

from rocking_notes import app
from rocking_notes.security_check import authenticate, identity

# initialize RestFul API
api = Api(app)
# initialize Json Web Token for API
# jwt = JWT(app, authenticate, identity)
jwt = JWTManager(app)
