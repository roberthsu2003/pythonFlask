from . import login

@login.route('/login', methods=['GET'])

def user_login():
    return "<h1>登入畫面</h1>"






