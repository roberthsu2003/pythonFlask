from flask import Flask

def createApp():
    app = Flask(__name__)
    @app.route("/")
    def index():
        return "<h1>Hello! World!</h1>"
    return app