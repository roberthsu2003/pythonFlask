from . import main
from .tools import getLot

from flask import render_template

@main.route("/")
def index():
    return render_template("main/index.html"),200

@main.route("/lot/<num>")
def lotWebPage(num):
    lotlist, specialNum = getLot()
    return render_template("main/lot.html",num=num,lot=lotlist,specialNum=specialNum),200