from flask import Flask

def createApp():
    app = Flask(__name__)
    @app.route("/")
    def index():
        return "Hello App"
    return app