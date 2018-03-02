#!/usr/bin/env python
# -*- coding: UTF-8 -*-# enable debugging

import cgi
import cgitb
cgitb.enable()

form_data = cgi.FieldStorage()

name = form_data.getvalue('name')
email = form_data.getvalue('email')

print ("""Content-type: text/html;charset=utf-8\r\n\r\n
        <!DOCTYPE html>
        <html>
            <head>
                <title>Server-side script</title>
            </head>
            <body>
                <p>In the NAME text box: {0} </p>
                <p>In the EMAIL text box: {1} </p>
            </body>
        </html>
        """.format(name, email))


