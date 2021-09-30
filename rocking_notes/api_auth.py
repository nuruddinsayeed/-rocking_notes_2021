from flask_jwt_extended.utils import create_access_token
from flask_restful import Resource
from peewee import IntegrityError
from rocking_notes import auth
from flask import request


#########################################################################
############### Authentication api Resource classes #####################
#########################################################################

class Login(Resource):
    """Login user and provide token"""

    def post(slef):
        try:
            username = request.json.get('username', None)
            password = request.json.get('password', None)

            if not username:
                return 'Missing username', 400
            if not password:
                return 'Missing password', 400

            # user_model = auth.get_user_model()
            # user = user_model.get(user_model.username == username)

            # if not user:
            #     return 'User Not Found!', 404

            if auth.authenticate(username, password):
                access_token = create_access_token(
                    identity={"username": username})
                return {'access_token': access_token}
            return 'Wrong User name Or Password!', 400
        except AttributeError:
            return 'Provide an Username and Password in JSON format in the request body', 400


class Register(Resource):
    """Define Registration via api"""

    def post(self):
        try:
            username = request.json.get('username', None)
            email = request.json.get('email', None)
            password = request.json.get('password', None)

            if not username:
                return 'Missing username', 400
            if not email:
                return 'Missing email', 400
            if not password:
                return 'Missing password', 400

            user = auth.User(
                username=username, email=email, active=True)
            user.set_password(password)
            user.save()

            access_token = create_access_token(identity={"username": username})
            return {"access_token": access_token}, 200
        except IntegrityError:
            return 'User Already Exists', 400
        except AttributeError:
            return 'Provide an Email and Password in JSON format in the request body', 400
