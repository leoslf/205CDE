#!/usr/bin/env python
# -*- coding: UTF-8 -*-# enable debugging

import cgi
import cgitb

cgitb.enable(True)

#print ('Content-Type: text/html;charset=utf-8\r\n\r\n')
#print ('<!DOCTYPE html>')
#print ('<html>')
#print ('<head>')
#print ('</head>')
#print ('<body>')
#
try:
    cgi.test()
except Exception as e:
    print ("Exception: " + str(e))

#print ('</body>')
#print ('</html>')

