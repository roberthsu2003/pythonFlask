from . import main
from flask import render_template

@main.route("/")
def index():
    return render_template("main/index.html"),200

@main.route("/lot/<num>")
def lot(num):
    return render_template("main/lot.html",num=num),200