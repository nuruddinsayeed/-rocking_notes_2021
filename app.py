from rocking_notes import app
from rocking_notes.admin import auth, admin

from rocking_notes.models import Note, Tag, NotesTags
from rocking_notes.api_config import api
from rocking_notes.api import All_public_notes, All_user_notes, Login, Register


# setup admin
admin.setup()
# add api endpoints
api.add_resource(Login, '/api/login')
api.add_resource(Register, '/api/register')
api.add_resource(All_public_notes, '/api/all-notes')
api.add_resource(All_user_notes, '/api/notes')

# simple utility function to create tables
# def create_tables():
#     with db:
#         db.create_tables(
#             [auth.User, Note, Tag, Note.tags.get_through_model()])


if __name__ == '__main__':
    auth.User.create_table(fail_silently=True)
    Note.create_table(fail_silently=True)
    Tag.create_table(fail_silently=True)
    NotesTags.create_table(fail_silently=True)
    # Course.students.get_through_model()

    # create_tables()

    app.run()
