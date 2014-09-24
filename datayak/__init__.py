from flask import Flask
from config import *
from pymongo import MongoClient

def connect_db():
    c = MongoClient(DATABASE['HOST'],DATABASE['PORT'])
    c = c.DATABASE['NAME']
    
    return c

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    

