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
        print ("Exception:" + str(e) + "<br />")
        print ("cannot get DB connection<br />")

    return conn

#if __name__ == "__main__":
#    header()
#    print (database_credential.db.items())

def query(table,
          column="*",
          condition="",
          join=""):
    conn = db_conn()
    assert(conn is not None)
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT %s FROM %s" % (column, table)
             + ((" WHERE " + condition) if condition != "" else "")
             + ((" INNER JOIN " + join) if join != "" else ""))

        result = {"description" : cursor.description, "rows" : cursor.fetchall()}
        return result
    except Exception as e:
        print ("Exception: " + str(e) + "<br />")
    finally:
        cursor.close()
        conn.close()

    return None


