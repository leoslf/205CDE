import sys
import os
import traceback
import json
try:
    from urlparse import urlparse
except ImportError:
    from urllib.parse import urlparse

from flask import *

from crm.db_connection import *

# helper functions
def rootpath(path=""):
    return os.path.dirname(os.path.abspath(__file__)) + "/" + path

def logged_in():
    return all(x in session for x in ("username", "displayed_username"))

def authentication(err_msg=None):
    if logged_in():
        try:
            # 2 == manager, 3 == admin
            msg = []
            results = query("staff", condition="username = '%s' AND (role+0) >= 2" % session["username"], err_msg=msg)
            print (results)
            if results is None and err_msg is not None and isinstance(msg, list) and len(msg) > 0:
                err_msg.append(msg[0])

            if len(results) == 1:
                # successful
                return True
        except:
            tb = traceback.format_exc()
            error("authentication Exception: in query, username: %s : " % session["username"] + str(tb))
            if err_msg is not None:
                assert (isinstance(err_msg, list))
                err_msg.append(tb)

    
    return False

def errmsg(msg, page="error.html", f=render_template):
    resp = make_response(f(urlparse(str(page)).path))
    resp.set_cookie("errmsg", str(msg))
    return resp

