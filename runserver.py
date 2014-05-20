#import os
#from app import create_app
#app = create_app(os.getenv('FLASK_CONFIG_NAME') or 'default')

from app import app

if __name__ == '__main__':
	app.run()

""" 
TODO LIST
---------
* wrapper over raw virtualenv
* blueprints + create_app factory
* 404 / 500 routes
* logging
* url joiner in requests

Done
----
* flask-bootstrap
* config.py SECTRET_KEY = "secret squirrel"

"""