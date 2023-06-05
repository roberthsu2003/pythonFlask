from flask import Blueprint,render_template

api1 = Blueprint("api",__name__,url_prefix="/api",template_folder="templates",static_folder="static")
from . import youbike,error,stockCode

@api1.route("/")
def api():
    return render_template('api.html')


