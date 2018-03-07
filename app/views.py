#!/usr/bin/env python

import sys
import os
from flask import *
from jinja2 import TemplateNotFound
from app import app as application
from app.utils import *

@application.before_request
def before_request():
    g.app_name = "205CDE"
    g.authentication = authentication

# matching route and handler
@application.route("/", defaults={"filename": "index.html"})
@application.route("/<path:filename>", methods = ["GET", "POST"])
def display(filename):
    try:
        return render_template(filename)
    except TemplateNotFound:
        return application.send_static_file(filename)

@application.route("/settings")
def settings():
    return render_template("settings.html")

@application.route("/login", methods = ["POST", "GET"])
def login():
    content = ""
    # Login Already 
    if logged_in():
        return redirect("/")

    if request.method == "POST":
        # login form submitted
        result = None
        try:
            results = query("staff", "CONCAT(firstname, ' ', lastname) AS name", "username='%s' AND password='%s'" % (request.form["username"], request.form["password"]))

            # login successful
            if len(results) == 1: 
                session["username"] = request.form["username"]
                session["displayed_username"] = results[0]["name"]
                return redirect(request.referrer)

            if len(results) == 0:
                msg = "Invalid username or password"
            else:
                msg = "Login Error (DB), returned number of rows > 1"
            msg += str(results)

        except Exception as e:
            application.logger.error("Exception in login: " + str(e))
            msg = "Exception occured during login query: " + str(e)

        return errmsg(msg, "login.html")

    # before login
    # GET Request
    return render_template("login.html")

@application.route("/logout")
def logout():
    # remove cookie variable
    for x in ("username", "displayed_username"):
        session.pop(x, None)
    return redirect(request.referrer)


