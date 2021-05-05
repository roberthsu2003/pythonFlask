import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def creatApp():
    app = Flask(__name__)
    #註冊Blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    #初始化flask_sqlalchemy
    basedir = os.path.abspath(os.path.dirname(__name__))
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir,'cities.sqlite')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)
    return app