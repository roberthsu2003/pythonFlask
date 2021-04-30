from flask import Flask

def createApp():
    app = Flask(__name__)

    app.config['SECRET_KEY'] = 'hardtoguessstring'

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from .login import login as login_blueprint
    app.register_blueprint(login_blueprint,url_prefix="/login")

    from .form import form as form_blueprint
    app.register_blueprint(form_blueprint,url_prefix="/form")

    return app