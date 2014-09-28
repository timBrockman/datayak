import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = "8585143a612fb2b28f308bc334fa978c10cf6ab1"
    #MEETUP API SETTINGS
    API_KEY = '7149703c352d601e6401c62421802f'
    MEMBER_ID = '169740182'
    
    
class LocalConfig(Config):
    DEBUG = True
    
    #MONGO SETTINGS
    MONGO_DBNAME='datayak'
    MONGO_HOST='localhost'
    MONGO_PORT='27017'
    
   
config = {
          'local': LocalConfig,
          'default': LocalConfig,
        } 