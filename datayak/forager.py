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
        # only params specifies the fields we want        
        only = 'category,city,created,description,id,organizer,topics,name,members'
        params = {
                  'sign':'true', 
                  'key':app.config['API_KEY'], 
                  'text':'technology',
                  'zip':'32801', 
                  'radius':'30', 
                  'page':'999',
                  'only':only
                  }
        
        # Make the API Request, transform response to native Python Types
        response = requests.get(url,params=params).json()
        
        #create empty list
        groups = []
        
        # ensure each group is unique, and add to the list        
        for group in response:        
            #check if the group exists in our db. If so, skip it
            doc = mongo.db.groups.find_one({'id':group['id']})
            if not doc:
                groups.append(group)
            else:
                pass
        
        #bulk insert to mongodb if list is not empty
        if groups:
            mongo.db.groups.insert(groups)
        else:
            print 'List is empty. No additional groups found'
                     
        print 'completed'
        
        return response