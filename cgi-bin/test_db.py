#!/usr/bin/env python
# -*- coding: UTF-8 -*-# enable debugging

from page_helper import *
from db_connection import db_conn

cgitb.enable()

conn = db_conn()
cur = conn.cursor()
header()
print ("<!DOCTYPE html>")
print ("<html>")
print ("<body>")
print ("</body>")
print ("</html>")

