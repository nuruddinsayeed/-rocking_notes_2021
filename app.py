from rocking_notes import app
from rocking_notes.admin import auth, admin
from rocking_notes.models import Note


# setup admin
admin.setup()

if __name__ == '__main__':
    auth.User.create_table(fail_silently=True)
    Note.create_table(fail_silently=True)
    app.run()
