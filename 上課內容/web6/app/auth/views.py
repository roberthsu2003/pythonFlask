from . import auth

@auth.route('/login')
def login():
    return "<h1>Hello!Login</h1>"