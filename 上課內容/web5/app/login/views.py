from . import login

@login.route("/")
def login():
    return "<h1>Login</h1>"