#!/usr/bin/env python
import sys
sys.path.insert(0, "../../http_credential")
from database_credential import db

class Config(object):
    DEBUG = False
    TESTING = False
    DATABASE_URI = 'mysql://%s@%s/%s' % (db['user'], db['host'], db['db'])

class ProductionConfig(Config):
    pass

class DevelopmentConfig(Config):
    DEBUG = True

class TestingConfig(Config):
    TESTING = True
