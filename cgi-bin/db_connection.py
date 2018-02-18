#!/usr/bin/env python
# -*- coding: UTF-8 -*-# enable debugging

import sys
sys.path.insert(0, "../../../http_credential")
import database_credential
from page_helper import *
from logging import *
from collections import OrderedDict
import pymysql
from pymysql.cursors import DictCursorMixin, Cursor

class OrderedDictCursor(DictCursorMixin, Cursor):
    dict_type = OrderedDict




def db_conn():
    """get database connection"""
    conn = None

    try:
        conn = pymysql.connect(**database_credential.db, cursorclass=OrderedDictCursor)
    except Exception as e:
        print ("Exception:", e, "<br />")
        print ("cannot get DB connection<br />")

    return conn

if __name__ == "__main__":
    header()
    print (database_credential.db.items())
