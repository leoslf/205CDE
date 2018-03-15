#!/usr/bin/env python
# -*- coding: UTF-8 -*-# enable debugging

import sys
sys.path.insert(0, "../../http_credential")
import database_credential
from logging import *
import traceback
from collections import OrderedDict
import re
import pymysql
from pymysql.cursors import DictCursorMixin, Cursor

class OrderedDictCursor(DictCursorMixin, Cursor):
    dict_type = OrderedDict

def db_conn():
    """get database connection"""
    conn = None

    try:
        conn = pymysql.connect(cursorclass=OrderedDictCursor, **database_credential.db)
    except Exception as e:
        print ("Exception:" + str(e) + "<br />")
        print ("cannot get DB connection<br />")

    return conn

def query(table,
          column="*",
          condition="",
          join="",
          desc=False,
          orderby=None,
          filter=None,
          err_msg=None):

    sql = "SELECT %s FROM %s" % (column, table) \
            + (" ORDER BY " + orderby if orderby is not None else "") \
            + (" WHERE " + condition if condition != "" else "") \
            + (" INNER JOIN " + join if join != "" else "")
    print (sql)

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
            columns = list(zip(*cursor.description))[0]
            return rows if desc == False else OrderedDict([("rows", rows), ("description", cursor.description), ("columns", columns)])
    except:
        tb = traceback.format_exc()
        error("Exception: " + str(tb) + "<br />")
        if err_msg is not None:
            print ("err_msg is not None")
            assert (isinstance(err_msg, list))
            err_msg.append(tb)
            print (err_msg)
    finally:
        conn.close()

    return None

def column_enum(table, column):
    sql = """
        SELECT COLUMN_TYPE 
        FROM information_schema.`COLUMNS` 
        WHERE TABLE_NAME = '%s' AND COLUMN_NAME = '%s'""" % (table, column)
    
    conn = db_conn()
    assert(conn is not None)

    try:
        with conn.cursor() as cursor:
            cursor.execute(sql)

            rows = cursor.fetchone()
            assert (len(rows) == 1)
            print (rows["COLUMN_TYPE"])
            values_str = re.search("\\(([^\\)]+)\\)", rows["COLUMN_TYPE"])
            values = values_str.group(1).split(",")
            values = [re.match("'([^']+)'", s).group(1) for s in values]
            return values

    except:
        tb = traceback.format_exc()
        error ("Exception: " + str(tb) + "<br />")
    finally:
        conn.close()

    return None
 
def insert(table,
           columns="",
           values="",
           errmsg=None):

    if columns == "" and isinstance(values, dict):
        columns = "(" + ", ".join(map(str, values.keys())) + ")"
        values = ", ".join(["'%s'" % x for x in values.values()])

    elif columns != "" and isinstance(values, str):
        # comma delimited string
        columns = "("+ columns +")"
    elif isinstance(values, list):
        values = ", ".join(["'%s'" % x for x in values])
    else:
        if errmsg is not None and errmsg is list:
            errmsg.append("values provided is neither dictionary with columns nor string paired with columns nor list paired with columns")
        return -1

    sql = "INSERT INTO " + table + " " \
            + columns \
            + " VALUE ("+ values +")"
    debug(sql)

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
           values,
           condition="",
           errmsg=None):

    col_n_val = ", ".join(["%s = '%s'" % (column, values[column]) for column in values])

    sql = "UPDATE " + table \
            + " SET " + col_n_val \
            + ((" WHERE " + condition) if condition != "" else "")

    print (sql)
    
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
        print (msg)
        # error(msg)
    finally:
        conn.close()

    return -1

def delete(table,
           condition="",
           errmsg=None):
    
    sql = ("DELETE FROM " + table \
            + ((" WHERE " + condition) if condition != "" else ""))
    debug(sql)
    
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
