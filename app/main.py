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
#app = Flask(__name__, template_folder=rootpath('templates'), static_url_path="/app/static")
app = Flask(__name__, template_folder=rootpath('templates'))
app.config.from_object(DevelopmentConfig)
app.secret_key = 'KEY'

@app.before_request
def before_request():
    g.nav = query("navigation")

# matching route and handler
@app.route('/')
def root():
    return render_template('index.html')

@app.route('/<filename>', methods = ['GET', 'POST'])
def send_static(filename):
    return app.send_static_file(filename)

@app.route('/css/<path>')
def send_css(path):
    return send_from_directory('css', path)

@app.route('/js/<path>')
def send_js(path):
    return send_from_directory('js', path)

@app.route("/login", methods = ['POST', 'GET'])
def login():
    content = ""
    # Login Already 
    if 'user' in session and 'displayed_username' in session:
        return redirect(url_for('root'))

    if request.method == "POST":
        # login form submitted
        result = None
        try:
            result = query("staff", "CONCAT(firstname, ' ', lastname) AS name", "username='%s' AND password='%s'" % (request.form['username'], request.form['password']))
        except Exception as e:
            return "Exception: " + str(e)

        # login successful
        if len(result["rows"]) == 1: 
            session['user'] = request.form['username']
            session['displayed_username'] = result["rows"][0]['name']
            return redirect(request.referrer)
        print (result)
        if len(result["rows"]) > 1:
            errmsg = "Login Error, returned number of rows > 1"
        errmsg = "Invalid username or password"
        resp = make_response(render_template('login.html'))
        resp.set_cookie('errmsg', errmsg)
        return resp
    # before login
    return render_template('login.html')

@app.route("/logout")
def logout():
    session.pop('user', None)
    session.pop('displayed_username', None)
    return redirect(request.referrer)

# prevent execution when this module is imported by others
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)

