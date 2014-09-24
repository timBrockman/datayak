import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = "8585143a612fb2b28f308bc334fa978c10cf6ab1"
    
class LocalConfig(Config):
    DEBUG = True
    DATABASE = {
              NAME:'datayak',
              USERNAME:'theyak',
              PASSWORD:'',
              HOST:'locahost',
              PORT:':27017',
              }
   
config = {
          'local': LocalConfig,
          'default': LocalConfig,
        } 