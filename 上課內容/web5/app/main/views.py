from . import main
from .tools import getLot
from flask import render_template
from flask import request

@main.route("/")
def index():
    return render_template("main/index.html"),200


@main.route("/lot",methods=["POST","GET"])
def lotWebPage():
    if request.method == "POST":
        num = int(request.values['count'])
    else:
        num = 12
    lots = [getLot() for _ in range(num)]
    return render_template("main/lot.html",num=num,lots=lots),200