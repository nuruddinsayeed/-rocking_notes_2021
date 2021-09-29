from flask_jwt_extended.utils import create_access_token
from flask_restful import Resource
from peewee import IntegrityError
from rocking_notes import auth
from flask_jwt import jwt_required
from flask import request

from rocking_notes.models import Note


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

            user_model = auth.get_user_model()
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


def note_dictionary(notes):
    """Convert Note object to Dictionary"""
    notes_list = []
    for note in notes:
        tags = []
        if note.tags:
            tags = [tag.tag_name for tag in note.tags]
        notes_list.append({
            'user': note.user.username,
            'tags': tags,
            'message': note.message,
            'public': note.public
        })
    return notes_list


class All_public_notes(Resource):
    """Response all public notes"""

    def get(self):
        """Hndle GET request"""
        notes_public = Note.select().where(Note.public)

        if notes_public:
            notes = note_dictionary(notes_public)

            return {'All Notes': notes}
        # If notes database is impty
        return {'notes': None}, 404


class All_user_notes(Resource):
    """Response All User Notes"""

    user = auth.get_user_model().get(1)

    @jwt_required()
    def get(self):
        """Response all users Notes"""

        # alu = get_jwt_identity()
        # print(f"=-{alu}---------->{self.user.username}")
        user_notes = Note.select().where(Note.user == self.user)

        if user_notes:
            return {"Your Notes": note_dictionary(user_notes)}
        return {'Your Notes': None}, 404
