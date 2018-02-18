#!/usr/bin/env python
# -*- coding: UTF-8 -*-# enable debugging

import pymysql
import sys
sys.path.insert(0, "../../../http_credential")
import database_credential
from logging import *


def db_conn():
    """get database connection"""
    conn = None

    try:
        print (*database_credential.db)
        conn = pymysql.connect(*database_credential.db)
    except Exception as e:
        print ("cannot get DB connection")

    return conn


