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
    
    url = 'https://api.meetup.com/2/groups.json'
    
    params = {
              'key':app.config['API_KEY'],
              'sign':'true',
              'member_id':app.config['MEMBER_ID'],
              }
    
    # Make the API Request
    data = requests.get(url,params=params)
    
    #convert JSON response to python dictionary
    data = data.json()
        
    datayak = {
               'name':name,
               'email':email,
               'password':password,
               'api_key':api_key,
               'groups':''
               }