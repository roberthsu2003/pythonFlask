from . import errors
from flask import render_template

@errors.app_errorhandler(404)
def page_not_found(e):
    return render_template('errors/index.html'), 404


