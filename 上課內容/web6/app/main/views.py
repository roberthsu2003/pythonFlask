from . import main
from flask import render_template
from ..model import db


@main.route("/")
def index():
    return render_template('index.html'),200

@main.route("/second")
def second():
    return render_template('second.html'),200