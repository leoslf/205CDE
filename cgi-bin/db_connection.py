#!/usr/bin/env python
# -*- coding: UTF-8 -*-# enable debugging

import pymysql
import sys
sys.path.insert(0, "../../../http_credential")
from database_credential import *
from logging import *


def db_conn():
    """get database connection"""
    conn = None

    try:
        for key, value in db.items():
            print ((key, value))
        print (db + "\r\n")
        conn = pymysql.connect(*db)
    except Exception as e:
        print ("cannot get DB connection\r\n")

    return conn


