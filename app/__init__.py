from flask import Flask
from flask_bootstrap import Bootstrap
from config import config

#print "__name__: {}".format(__name__)

app = Flask(__name__)
app.config.from_object(config['default'])
Bootstrap(app)

from . import views
#print app.view_functions

"""
def create_app(config_name):
	app = Flask(__name__)
	app.config.from_object(config[config_name])
	Bootstrap(app)
	from app import views
	app.register_blueprint(views)
	return app

"""