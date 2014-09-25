import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = "8585143a612fb2b28f308bc334fa978c10cf6ab1"
    
class LocalConfig(Config):
    DEBUG = True
    
    #MONGO SETTINGS
    MONGO_DBNAME='datayak'
    MONGO_HOST='locahost'
    MONGO_PORT='27017'
    
   
config = {
          'local': LocalConfig,
          'default': LocalConfig,
        } 