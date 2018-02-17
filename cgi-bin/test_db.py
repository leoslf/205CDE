#!/usr/bin/env python
# -*- coding: UTF-8 -*-# enable debugging

import cgi
import cgitb
from db_connection import db_conn

cgitb.enable()

print (db_conn())
