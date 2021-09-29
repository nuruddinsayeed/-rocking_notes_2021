from rocking_notes import app, db
from rocking_notes.admin import auth, admin
from rocking_notes.models import Note, Tag, NotesTags
from rocking_notes.api import api


# setup admin
admin.setup()
# setup API
# configure the urls
api.setup()


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
