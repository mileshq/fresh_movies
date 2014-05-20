from flask import Flask
from flask_bootstrap import Bootstrap
import config

app = Flask(__name__)
app.config.from_object(config.config['default'])
Bootstrap(app)

"""
def create_app(config_name):
	app = Flask(__name__)
	app.config.from_object(config.config[config_name])
	Bootstrap(app)

	return app
"""
from app import views