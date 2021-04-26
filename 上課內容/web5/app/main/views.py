from . import main
from .tools import getLot

from flask import render_template

@main.route("/")
def index():
    return render_template("main/index.html"),200

@main.route("/lot/<int:num>")
def lotWebPage(num):
    lots = [getLot() for _ in range(num)]
    return render_template("main/lot.html",num=num,lots=lots),200