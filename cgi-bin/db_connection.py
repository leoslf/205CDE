#!/usr/bin/env python
# -*- coding: UTF-8 -*-# enable debugging

import pymysql
import sys
sys.path.insert(0, "../../http_credential")
import database_credential
import logging


def db_conn():
    """get database connection"""
    conn = None

    try:
        conn = pymysql.connect(*database_credential.db)
    except Exception as e:
        error("cannot get DB connection")

    return conn


