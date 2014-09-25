from flask import Flask
from config import config
from .models import mongo

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    # Flask-PyMongo Reads from Config to establish connections
    mongo.init_app(app)
    
    return app

