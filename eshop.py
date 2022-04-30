# eshop.py
# made by lambda
# this is the base line flask code that deals with setting up everything correctly
# inspired by WiiLink24's room-server room.py

# imports
# import flask
from flask import flask
# import loginmanager for the admin panel
from flask_login import LoginManager
from flask_migrate import Migrate
from sqlalchemy_searchable import make_searchable

from models import db, login

import config

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = config.db_url
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SECRET_KEY"] = config.secret_key

db.init_app(app)
make_searchable(db.metadata)

migrate = Migrate(app, db)
login.init_app(app)

@app.before_first_request
def initialize_server():
    # Ensure our database is present.
    db.create_all()

db.configure_mappers()

# import routes

import ias
import ninja
import ecs
import samurai