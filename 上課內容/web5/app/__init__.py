from flask import Flask
import os
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def createApp():
    app = Flask(__name__)

    app.config['SECRET_KEY'] = 'hardtoguessstring'

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from .login import login as login_blueprint
    app.register_blueprint(login_blueprint,url_prefix="/login")

    from .form import form as form_blueprint
    app.register_blueprint(form_blueprint,url_prefix="/form")
    #database
    basedir = os.path.abspath(os.path.dirname(__file__))
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)

    return app