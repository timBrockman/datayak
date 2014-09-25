from flask import Flask
from config import *
from flask.ext.pymongo import PyMongo


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    # Flask-PyMongo Reads from Config to establish connections
    mongo=PyMongo(app)
    
    return app

