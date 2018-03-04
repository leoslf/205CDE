import os
from flask import Flask
from .config import DevelopmentConfig
from .db_connection import *
from .blueprints.admin import admin

# instantiate a Flask object
app = Flask(__name__)
app.config.from_object(DevelopmentConfig)
app.register_blueprint(admin, url_prefix="/admin")
app.secret_key = "KEY"
app.jinja_env.globals.update(zip=zip, list=list, query=query)

from app import views, models
