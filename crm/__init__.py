import os
from logging import basicConfig
from flask import Flask
from crm.config import DevelopmentConfig
from crm.db_connection import *
from crm.blueprints.admin import admin

# instantiate a Flask object
app = Flask(__name__)
app.config.from_object(DevelopmentConfig)
app.register_blueprint(admin, url_prefix="/admin")
app.secret_key = "KEY"
# enable these functions in templates
app.jinja_env.globals.update(zip=zip, list=list, str=str, query=query)
# Trim Empty Lines
app.jinja_env.trim_blocks = True
app.jinja_env.lstrip_blocks = True

basicConfig(filename="log.log")

# Circular import 
from crm import views, models
