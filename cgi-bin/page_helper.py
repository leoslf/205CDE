#!/usr/bin/env python
# -*- coding: UTF-8 -*-# enable debugging

import cgi
import cgitb

def header():
    print ('Content-Type: text/html;charset=utf-8\r\n\r\n')

if __name__ != "__main__":
    cgitb.enable()


