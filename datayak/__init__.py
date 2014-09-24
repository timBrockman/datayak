from flask import Flask

app = Flask(__name__)
app.config["SECRET_KEY"] = "8585143a612fb2b28f308bc334fa978c10cf6ab1"

if __name__ == '__main__':
	app.run()
