from flask import Flask
from flask_peewee.db import Database
from flask_peewee.auth import Auth


# Setup Database ----->
# configure our database
DATABASE = {
    'name': 'notes.db',
    'engine': 'peewee.SqliteDatabase',
}

DEBUG = True
SECRET_KEY = 'hin6bab8ge25*r=x&amp;+5$0kn=-#log$pt^#@vrqjld!^2ci@g*b'
JWT_SECRET_KEY = 'hin6bab8ge25*r=x&amp;+5$0kn=-#log$pt^#@vrqjld!^2ci@g*b'

# Create main App ----->
app = Flask(__name__)
app.config.from_object(__name__)


# instantiate the db wrapper
db = Database(app)
auth = Auth(app, db)
# admin = Admin(app, auth)
