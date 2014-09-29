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
        
        # create API query
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
        
        #create empty list
        groups = []
        
        # ensure each group is unique, and add to the list        
        for group in response:        
            #check if the group exists in our db. If so, skip it
            doc = mongo.db.groups.find_one({'id':group['id']})
            if group['id'] == doc['id']:
                pass
            else:
                groups.append(group)
        
        #bulk insert to mongodb if list is not empty
        if groups:
            mongo.db.groups.insert(groups)
        else:
            print 'List is empty. No additional groups found'
                     
        print 'completed'
        
        return response