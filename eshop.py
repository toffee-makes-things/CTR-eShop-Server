# eshop.py
# made by lambda
# this is the base line flask code that deals with setting up everything correctly
# inspired by WiiLink24's room-server room.py

# imports
# import flask
from flask import flask
# import loginmanager for the admin panel
from flask_login import LoginManager

from models import db, login

import config












# import routes

import ias
import ninja
import ecs
import samurai