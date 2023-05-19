from . import auth

@auth.route("/login")
def login():
    return "Hello! Login"