import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def creatApp():
    app = Flask(__name__)
    #註冊Blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint,url_prefix='/auth')
    #初始化flask_sqlalchemy
    basedir = os.path.abspath(os.path.dirname(__file__))

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+ os.path.join(basedir,'cities.sqlite')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    #防止CSRF的攻擊
    app.config["SECRET_KEY"] = "lkjkdfjikjhKlkdsjfdksKSLIhjlsdkjairywtyslvkd"
    db.init_app(app)
    return app