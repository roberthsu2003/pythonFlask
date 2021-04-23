from flask import Flask,render_template

def creatApp():
    app = Flask(__name__)
    @app.route("/",methods=["GET","POST"])
    def index():
        return render_template("index.html"),200

    @app.route("/name", methods=["GET", "POST"])
    def name():
        return render_template("name.html",), 200

    @app.route("/username/<name>",methods=["GET","POST"])
    def username(name):
        return render_template("username.html",name=name,greet="Hello!"),200
    return app