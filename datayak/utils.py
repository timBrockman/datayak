# datayak utils
from flask.ext.pymongo import PyMongo
from datayak import app, mongo
import bson, requests, json

def upsert_yak():
    """
    Creates the Yak document if it doesn't exist. 
    Or, Updates the existing Yak document to remain current with
    his groups
    """

    url = 'https://api.meetup.com/2/profiles.json'
    
    params = {
              'key':app.config['API_KEY'],
              'sign':'true',
              'member_id':app.config['MEMBER_ID'],
              }

    r = requests.get(url,params=params)
        
    datayak = {
               'name':name,
               'email':email,
               'password':password,
               'api_key':api_key,
               'groups':''
               }