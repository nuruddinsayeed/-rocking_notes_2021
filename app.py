from rocking_notes import app
from rocking_notes.admin import auth, admin
from rocking_notes.models import Note, Tag
from rocking_notes.api import api


# setup admin
admin.setup()
# setup API
# configure the urls
api.setup()

if __name__ == '__main__':
    auth.User.create_table(fail_silently=True)
    Note.create_table(fail_silently=True)
    Tag.create_table(fail_silently=True)
    app.run()
