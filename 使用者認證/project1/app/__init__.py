import os
from flask import Flask
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
login_manager = LoginManager()
login_manager.login_view = 'auth.login'

bootstrap = Bootstrap()

db = SQLAlchemy()
#執行一次models
#from . import models
def create_app():
    app = Flask(__name__)
    basedir = os.path.abspath(os.path.dirname(__file__))
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix='/auth')

    # Flask-Login
     # 告知果到保護的頁面必需到Blueprint.function
    login_manager.init_app(app)
    bootstrap.init_app(app)

    @app.route("/")
    def index():
        return "Hello!Jenny"

    from flask_login import login_required
    @app.route('/secret')
    @login_required
    def secret():
        return "只有認證通過的使用者可以看到這個頁面"

    return app

