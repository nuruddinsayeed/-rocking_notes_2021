from flask_peewee.rest import RestAPI
from rocking_notes import app, auth

from rocking_notes.models import Note
from rocking_notes.resources import UserResource, NoteResource


# Iinitialize api with peewee api wrapper
api = RestAPI(app)

# register our models so they are exposed via /api/<model>/
api.register(auth.User, UserResource)
api.register(Note, NoteResource)
