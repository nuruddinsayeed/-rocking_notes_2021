from flask_peewee.admin import Admin
import datetime
from flask import Flask
from flask_peewee.auth import Auth
from flask_peewee.db import Database
from peewee import *

# Setup Database ----->
# configure our database
DATABASE = {
    'name': 'sqlitedb.db',
    'engine': 'peewee.SqliteDatabase',
}

# Create main App ----->
app = Flask(__name__)
app.config.from_object(__name__)

# instantiate the db wrapper
db = Database(app)


class Note(db.Model):
    message = TextField()
    created = DateTimeField(default=datetime.datetime.now)


# create an Auth object for use with our flask app and database wrapper
auth = Auth(app, db)

admin = Admin(app, auth)
admin.register(Note)

admin.setup()


if __name__ == '__main__':
    auth.User.create_table(fail_silently=True)
    Note.create_table(fail_silently=True)

    app.run()
