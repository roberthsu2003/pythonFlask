from flask import Flask,request

app = Flask(__name__)

@app.route("/")
def index():
    message = "<h1>request headers</h1>"
    message += f"<ul><li>host:{request.headers.get('Host')}</li>"
    message += f"<li>host_url:{request.headers.get('host_url')}</li>"
    message += f"<li>user_agent:{request.headers.get('User-Agent')}</li>"
    message +=  f"<li>Accept-Language:{request.headers.get('Accept-Language')}</li></ul>"
    return message
    