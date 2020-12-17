import flask
from newsletter_builder import *

app = flask.Flask(__name__)

@app.route("/")
def index():
    newsletter = generate_updated_newsletter()
    return newsletter

app.run(host="0.0.0.0",port=9999)