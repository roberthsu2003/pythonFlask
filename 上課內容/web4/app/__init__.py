from flask import Flask,render_template

def creatApp():
    app = Flask(__name__)
    @app.route("/",methods=["GET","POST"])
    def index():
        return render_template("index.html"),200
    return app