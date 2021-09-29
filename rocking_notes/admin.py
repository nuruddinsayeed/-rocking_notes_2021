from flask_peewee.admin import Admin
from rocking_notes import app, auth

from rocking_notes.models import Note


# register admin
admin = Admin(app, auth)
admin.register(Note)
auth.register_admin(admin)
