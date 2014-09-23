from flask import Flask
from flask.ext.mongoengine import MongoEngine

app = Flask(__name__)
app.config["MONGODB_SETTINGS"] = {'DB': "datayak"}
app.config["SECRET_KEY"] = "8585143a612fb2b28f308bc334fa978c10cf6ab1"

db = MongoEngine(app)

if __name__ == '__main__':
	app.run()
