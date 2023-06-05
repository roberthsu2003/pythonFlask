from flask import Blueprint

api1 = Blueprint("api",__name__,url_prefix="/api")

@api1.route("/")
def api():
    return "Hello! 本目錄提供Web api"

@api1.route("/youbike")
def youbike():
    return "<h1>Hello! Youbike</h1>"

