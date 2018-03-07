import sys
import os
from urlparse import urlparse
from flask import *
from app.db_connection import *

# helper functions
def rootpath(path=""):
    return os.path.dirname(os.path.abspath(__file__)) + "/" + path

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

def errmsg(msg, page="error.html", f=render_template):
    resp = make_response(f(urlparse(str(page)).path))
    resp.set_cookie("errmsg", str(msg))
    return resp

