from flask import Flask
from flask.ext.bootstrap import Bootstrap
from config import config

DEBUG = True
app = Flask(__name__)

#app.config.from_object(__name__)
app.config.from_object(config['default'])
Bootstrap(app)

from app import views

"""
def create_app(config_name):
	app = Flask(__name__)
	app.config.from_object(config[config_name])
	Bootstrap(app)
	from app import views
	app.register_blueprint(views)
	return app

"""
