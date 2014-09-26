from flask.ext.pymongo import PyMongo
from datayak import mongo



class Yak(object):
    """
    The Yak Model represents a collection in mongo, which contains the Yak's data 
    including the groups he belongs to and his data.
    """
    
    # create dictionary keys for a Yak document
