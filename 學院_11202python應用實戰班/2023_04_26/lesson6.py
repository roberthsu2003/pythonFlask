from flask import Flask

app = Flask(__name__)

@app.route("/")
def abc():
    return "<h1>Hello! Flask!</h1>"