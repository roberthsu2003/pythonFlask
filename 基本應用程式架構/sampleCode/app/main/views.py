from . import main
from ..model import City
from flask import render_template

@main.route('/',)
def index():
    citys = City.query.all()
    return render_template('index.html',citys=citys)

@main.route('/container')
def container():
    return render_template('container.html')