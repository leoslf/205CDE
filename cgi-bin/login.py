#!/usr/bin/env python
# -*- coding: UTF-8 -*-# enable debugging

from page_helper import *
from db_connection import *

form = cgi.FieldStorage()
assert("username" in form)
assert("password" in form)

header()
print ("<!DOCTYPE html>")
print ("<html>")
print ("<body>")
#print (form)
#print ("<br />")
try:
    result = query("staff", "CONCAT(firstname, ' ', lastname) AS name", "username='%s' AND password='%s'" % (form['username'].value, form['password'].value))
    if len(result["rows"]) != 1:
        raise Exception("Login Error, returned number of rows != 1")
    print (result["rows"][0]['name']) 
    print ("<br />")
except Exception as e:
    print (e)
    print ("<br />")

print ("<br />")
print ("</body>")
print ("</html>")

