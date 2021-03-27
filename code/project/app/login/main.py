from . import login
from flask import render_template

@login.route('/login', methods=['GET'])

def user_login():
    return render_template("login/index.html")






