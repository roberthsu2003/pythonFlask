from flask import Flask,render_template

def createApp():
    app = Flask(__name__)
    @app.route("/")
    def index():
        return render_template("index.html")

    @app.route("/equalWidth")
    def equalWidth():
        return render_template("equalWidth.html")
    return app