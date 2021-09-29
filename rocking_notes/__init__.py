from flask import Flask
from flask_peewee.db import Database
from flask_peewee.auth import Auth
from flask_peewee.admin import Admin
from flask_migrate import Migrate


# Setup Database ----->
# configure our database
DATABASE = {
    'name': 'sqlitedb.db',
    'engine': 'peewee.SqliteDatabase',
}

# Creating secreat key for form cerf_token verification ----->
DEBUG = True
SECRET_KEY = 'MySuperSecretKey'

# Create main App ----->
app = Flask(__name__)
app.config.from_object(__name__)


# instantiate the db wrapper
db = Database(app)
# Migrate(app, db)  # to perform migrations on database and app
auth = Auth(app, db)
# admin = Admin(app, auth)
