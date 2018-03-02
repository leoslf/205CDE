#!/usr/bin/env python

from flask_script import Manager, Server
from main import app

# configure the app
manager = Manager(app)

# set `python manage.py runserver` as server start command
manager.add_command('runserver', Server())

# set `python manage.py shell` as server shell starting command
@manager.shell
def shell_context():
    return dict(app=app)

if __name__ == '__main__':
    manager.run()

