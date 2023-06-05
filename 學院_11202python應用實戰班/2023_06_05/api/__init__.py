from flask import Blueprint

api = Blueprint("api",__name__,url_prefix="/api")

@api.route("/")
def api():
    return "Hello! 本目錄提供Web api"

@api.route("/youbike")
def youbike():
    return "<h1>Hello! Youbike</h1>"

