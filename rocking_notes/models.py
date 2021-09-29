from rocking_notes import db
import peewee
from flask_peewee.auth import Auth
from rocking_notes import auth


# Database Model Classes

class Tag(db.Model):
    """Define tag model for Note tag"""

    tag_name = peewee.CharField(max_length=50)

    def __str__(self):
        return f"{self.tag_name}"


class Note(db.Model):
    """Define Users """

    user = peewee.ForeignKeyField(auth.get_user_model(), on_delete='CASCADE')
    tags = peewee.ManyToManyField(Tag, backref='notes')

    message = peewee.CharField(max_length=255)
    public = peewee.BooleanField(default=False)

    def __str__(self):
        return f"({self.get_id()}) User: {self.user.username} public: {self.public}"

    # def __repr__(self) -> str:
    #     return f"{self.message} public: {self.public}"


# Now For Many to Many relations
NotesTags = Note.tags.get_through_model()

# Flask db init
# flask db migrate -m ""
# from app import auth
# admin = auth.User(username='sayed', email='', admin=True, active=True)
# admin.set_password('123')
# admin.save()

# auth.User.create_table(fail_silently=True)  # make sure table created.
