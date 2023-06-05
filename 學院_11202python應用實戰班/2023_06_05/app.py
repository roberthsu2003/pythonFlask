from flask import Flask
from api import api1

app = Flask(__name__)
app.register_blueprint(api1, url_prefix='/api')

@app.route("/")
def index():
    return "<h1>Hello! 徐國堂!</h1>"

