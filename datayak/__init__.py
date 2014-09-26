from flask import Flask
from config import config
from flask.ext.pymongo import PyMongo

app = Flask(__name__)
app.config.from_object(config['local'])
# Flask-PyMongo Reads from Config to establish connections
mongo = PyMongo(app)
from .views import yak
app.register_blueprint(yak)