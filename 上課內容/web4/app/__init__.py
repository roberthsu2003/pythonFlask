from flask import Flask,render_template
import random

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

    @app.route('/table')
    def table():
        students = [[random.randint(50,100) for _ in range(5)] for _ in range(50)]
        return render_template("table.html",students = students),200
    return app