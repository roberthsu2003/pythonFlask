from . import main
from flask import render_template

@main.route("/")
def index():
    return render_template('index.html'),200