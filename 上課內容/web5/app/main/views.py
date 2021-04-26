from . import main
from flask import render_template
from random import randint

@main.route("/")
def index():
    return render_template("main/index.html"),200

@main.route("/lot/<num>")
def lotWebPage(num):
    lot = set()
    while(len(lot)<=7):
        lot.add(randint(1, 49))
    lotlist = list(lot)
    specialNum = lotlist.pop()
    return render_template("main/lot.html",num=num,lot=lotlist,specialNum=specialNum),200