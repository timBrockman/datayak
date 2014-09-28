# datayak utils
from flask.ext.pymongo import PyMongo
from datayak import mongo
import bson, requests, json
from config import config

def create_yak(name, email, password, api_key):
    
    groups = ''
        
    datayak = {
               _id: bson.ObjectId(),
               'name':name,
               'email':email,
               'password':password,
               'api_key':api_key,
               'groups':''
               }