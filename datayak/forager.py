from flask.ext.pymongo import PyMongo
from datayak import app, mongo
import requests, json

class Groups(object):
    """
    The Yak Model represents a collection in mongo, which contains the Yak's data 
    including the groups he belongs to and his data.
    """
    
    # create dictionary keys for a Yak document
    def find_groups(*args, **kwargs):
        """
        Perform raw_text search for groups containing technology in title, category, or description
        """
        
        url = 'https://api.meetup.com/find/groups'
        params = {
                  'sign':'true', 
                  'key':app.config['API_KEY'], 
                  'member_id':app.config['MEMBER_ID'], 
                  'text':'technology',
                  'zip':'32801', 
                  'radius':'30', 
                  'page':'999',
                  }

        
        # Make the API Request, transform response to native Python Types
        response = requests.get(url,params=params).json()
        
        # Save each group contained in the response as a Mongo document
        for group in response:
            if mongo.db.groups.find({'id':{'$exists': False}}):
                mongo.db.groups.insert(item)
            else:
                pass 
            
        print 'completed'
        
        return response