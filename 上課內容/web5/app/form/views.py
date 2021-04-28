from . import form
from flask import render_template

@form.route("/")
def form():
    return render_template("/form/index.html")