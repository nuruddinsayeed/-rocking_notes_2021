from rocking_notes import db
import peewee


# Database Model Classes
class Note(db.Model):
    """Define Users """

    message = peewee.CharField(max_length=255)

# Flask db init
# flask db migrate -m ""
