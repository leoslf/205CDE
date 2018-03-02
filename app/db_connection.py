#!/usr/bin/env python
# -*- coding: UTF-8 -*-# enable debugging

import sys
sys.path.insert(0, "../../http_credential")
import database_credential
from logging import *
from collections import OrderedDict
import pymysql

def db_conn():
    """get database connection"""
    conn = None

    try:
        conn = pymysql.connect(**database_credential.db)
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
          join="",
          desc=False,
          filter=None):

    sql = "SELECT %s FROM %s" % (column, table) \
            + ((" WHERE " + condition) if condition != "" else "") \
            + ((" INNER JOIN " + join) if join != "" else "")
    #debug(sql)

    conn = db_conn()
    assert(conn is not None)

    try:
        with conn.cursor() as cursor:
            cursor.execute(sql)

            #result = {"description" : cursor.description, "rows" : cursor.fetchall()}
            rows = cursor.fetchall()
            if filter is not None:
                rows = [item for item in rows \
                            if all(attrib not in item \
                                    or item[attrib] == filter[attrib]
                                for attrib in filter)]
            return rows if desc == False else OrderedDict(rows=rows, description=cursor.descrption)
    except Exception as e:
        print ("Exception: " + str(e) + "<br />")
    finally:
        conn.close()

    return None

def insert(table,
           column="",
           values="",
           errmsg=None):

    columns = (("(" + columns + ")") if columns != "" else "")
    sql = ("INSERT INTO " + table + " " + columns \
            + " VALUE (" + value + ")")
    #debug(sql)

    conn = db_conn()
    assert(conn is not None)
    try:
        with conn.cursor() as cursor:
            cursor.execute(sql)
            conn.commit()
            return cursor.lastrowid
    except Exception as e:
        msg = "MYSQLError: errno %r, %r" % (e.args[0], e)
        if errmsg is not None:
            errmsg.append(msg)
        # error(msg)
    finally:
        conn.close()

    return -1

def update(table,
           column_and_value="",
           condition="",
           errmsg=None):

    sql = ("UPDATE " + table + " SET " + column_and_value + ((" WHERE " + condition) if condition != "" else ""))
    #debug(sql)
    
    conn = db_conn()
    assert(conn is not None)

    try:
        with conn.cursor() as cursor:
            cursor.execute(sql)
            conn.commit()
            return cursor.rowcount
    except Exception as e:
        msg = "MYSQLError: errno %r, %r" % (e.args[0], e)
        if errmsg is not None:
            errmsg.append(msg)
        # error(msg)
    finally:
        conn.close()

    return -1

def delete(table,
           condition="",
           errmsg=None):
    
    sql = ("DELETE FROM " + table \
            + ((" WHERE " + condition) if condition != "" else ""))
    #debug(sql)
    
    conn = db_conn()
    assert(conn is not None)

    try:
        with conn.cursor() as cursor:
            cursor.execute(sql)
            conn.commit()
            return cursor.rowcount
    except Exception as e:
        msg = "MYSQLError: errno %r, %r" % (e.args[0], e)
        if errmsg is not None:
            errmsg.append(msg)
        # error(msg)
    finally:
        conn.close()

    return -1
