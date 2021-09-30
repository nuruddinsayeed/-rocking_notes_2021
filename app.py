from rocking_notes import app
from rocking_notes.admin import auth, admin

from rocking_notes.models import Note, Tag, NotesTags
from rocking_notes.api_config import api

from rocking_notes.api_auth import Login, Register
from rocking_notes.api_notes_list import (
    AllPublicNotes, NotesByTagPublic, AllUserNotes, NotesByTag
)
from rocking_notes.api_note_tag import TagResoruce, NoteResource


# setup admin
admin.setup()
# add api endpoints
api.add_resource(Login, '/api/login')
api.add_resource(Register, '/api/register')
api.add_resource(AllPublicNotes, '/api/all-notes')
api.add_resource(NotesByTagPublic, '/api/all-notes/<string:tag_name>')
api.add_resource(AllUserNotes, '/api/notes')
api.add_resource(NotesByTag, '/api/notes/<string:tag_name>')
api.add_resource(TagResoruce, '/api/tags')
api.add_resource(NoteResource, '/api/notes/<int:id>')


if __name__ == '__main__':
    auth.User.create_table(fail_silently=True)
    Note.create_table(fail_silently=True)
    Tag.create_table(fail_silently=True)
    NotesTags.create_table(fail_silently=True)
    # Course.students.get_through_model()

    # create_tables()

    app.run()
