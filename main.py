#!/usr/bin/env python

from flask import *
from config import DevelopmentConfig

# instantiate a Flask object
app = Flask(__name__)
app.config.from_object(DevelopmentConfig)

# matching route and handler
@app.route('/success/<name>')
def success(name):
    return "Welcome %s" % name

@app.route("/login", methods = ['POST', 'GET'])
def login():
    if request.method == 'POST':
        user = request.form['nm']
    else:
        user = request.args.get('nm')
    if user is None:
        user = "__None__"
    return redirect(url_for('success', name = user))

# prevent execution when this module is imported by others
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)

