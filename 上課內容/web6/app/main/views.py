from . import main
from flask import render_template
from ..model import db,createDB,City


@main.route("/")
def index():
    createDB()
    citys = City.query.limit(9).all()
    return render_template('index.html',citys=citys),200


@main.route("/second")
def second():
    return render_template('second.html'),200