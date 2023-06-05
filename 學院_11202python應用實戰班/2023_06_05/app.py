from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "<h1>Hello! 徐國堂!</h1>"

