from . import main
from flask import render_template
from ..model import db,createDB,City


@main.route("/")
def index():
    createDB()
    print(City.query.filter_by(country='Japan').all())
    return render_template('index.html'),200


@main.route("/second")
def second():
    return render_template('second.html'),200