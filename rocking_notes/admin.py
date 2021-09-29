from flask_peewee.admin import Admin
from rocking_notes import app, auth

from rocking_notes.models import Note, Tag, NotesTags


# register admin
admin = Admin(app, auth)
admin.register(Note)
admin.register(Tag)
admin.register(NotesTags)
auth.register_admin(admin)
