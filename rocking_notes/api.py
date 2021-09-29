from flask_peewee.rest import RestAPI, UserAuthentication, AdminAuthentication
from rocking_notes import app, auth

from rocking_notes.models import Note
from rocking_notes.resources import UserResource, NoteResource


# create an instance of UserAuthentication and AdminAuthentication
user_auth = UserAuthentication(auth)
admin_auth = AdminAuthentication(auth)
# Iinitialize api with peewee api wrapper
api = RestAPI(app, default_auth=user_auth)


# register our models so they are exposed via /api/<model>/

# response all user data
api.register(model=auth.User, provider=UserResource,
             allowed_methods=['GET', 'POST', 'PUT', 'DELETE'])

# response all public notes data
api.register(model=Note, provider=NoteResource, auth=user_auth,
             allowed_methods=['GET'])
