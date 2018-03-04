#!/usr/bin/env python

import sys
import os
from flask import *
from config import DevelopmentConfig
from db_connection import *

# helper functions
def rootpath(path=""):
    return os.path.dirname(os.path.abspath(__file__)) + "/" + path

# instantiate a Flask object
app = Flask(__name__, template_folder=rootpath("templates"))
app.config.from_object(DevelopmentConfig)
app.secret_key = "KEY"

def logged_in():
    return all(x in session for x in ("username", "displayed_username"))

def authentication():
    if logged_in():
        try:
            # 2 == manager, 3 == admin
            results = query("staff", condition="username = '%s' AND (role+0) >= 2" % session["username"])
            print (results)
            if len(results) == 1:
                # successful
                return True
        except Exception as e:
            app.logger.error("authentication Exception: in query, username: %s : " % session["username"] + str(e))
    
    return False

def errmsg(msg, page="error.html"):
    resp = make_response(render_template(str(page)))
    resp.set_cookie("errmsg", str(msg))
    return resp

@app.before_request
def before_request():
    g.app_name = "205CDE"
    g.nav = query("navigation", filter=dict(bar="shared"))
    g.cms_nav = query("navigation", filter=dict(bar="cms"))
    g.authentication = authentication
    g.query = query

# matching route and handler
@app.route("/")
def index():
    return render_template("index.html")

# Content Management System (CMS)
@app.route("/admin")
def admin():
    if logged_in() == False:
        return errmsg("Please login first")
    if authentication():
        return render_template("admin.html")
    return errmsg("You do not have permission to access this page")



@app.route("/<filename>", methods = ["GET", "POST"])
def send_static(filename):
    return app.send_static_file(filename)

@app.route("/login", methods = ["POST", "GET"])
def login():
    content = ""
    # Login Already 
    if logged_in():
        return redirect(url_for("index"))

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
            app.logger.error("Exception in login: " + str(e))
            msg = "Exception occured during login query: " + str(e)

        return errmsg(msg, "login.html")

    # before login
    return render_template("login.html")

@app.route("/logout")
def logout():
    # remove cookie variable
    for x in ("username", "displayed_username"):
        session.pop(x, None)
    return redirect(request.referrer)

# prevent execution when this module is imported by others
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)

