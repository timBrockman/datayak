from flask import Blueprint, render_template
from . import mongo
yak = Blueprint('simple_page',__name__, template_folder='templates')

@yak.route("/")
def test_yak():
    test_yak=mongo.db.testyaks.find_one()
    greeting = test_yak['greeting']
    return render_template('testyak.html',greeting=greeting)