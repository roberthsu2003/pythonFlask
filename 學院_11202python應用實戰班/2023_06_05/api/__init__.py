from flask import Blueprint

api1 = Blueprint("api",__name__,url_prefix="/api")
from . import youbike,error,stockCode

@api1.route("/")
def api():
    return "Hello! 本目錄提供Web api"


