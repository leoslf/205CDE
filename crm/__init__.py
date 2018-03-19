import os
from logging import *
from logging.handlers import *

import smtplib
from flask import Flask
from crm.config import *
from crm.db_connection import *
from crm.blueprints.admin import admin

# instantiate a Flask object
app = Flask(__name__)
app.config.from_object(DevelopmentConfig)
app.register_blueprint(admin, url_prefix="/admin")
app.secret_key = "KEY"
# enable these functions in templates
app.jinja_env.globals.update(zip=zip, list=list, str=str, query=query, isinstance=isinstance)
app.jinja_env.add_extension('jinja2.ext.do')
# Trim Empty Lines
app.jinja_env.trim_blocks = True
app.jinja_env.lstrip_blocks = True

basicConfig(filename="log.log", level=DEBUG)

SMTP_config = dict(
    mailhost = ("smtp.gmail.com", 587), 
    fromaddr = Config.admin_email, 
    toaddrs = Config.admin_email, 
    subject = "Critical/Error Event From %s" % Config.name,
    credentials=(Config.admin_email, Config.admin_email_pw)
)

email_handler = SMTPHandler(**SMTP_config)
email_handler.setlevel = ERROR
getLogger().addHandler(email_handler)

# Circular import 
from crm import views, models
