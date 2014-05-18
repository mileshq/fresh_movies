from flask import Flask
import config
from flask_bootstrap import Bootstrap

app = Flask(__name__)
app.config.from_object(config.config['default'])
Bootstrap(app)

from app import views