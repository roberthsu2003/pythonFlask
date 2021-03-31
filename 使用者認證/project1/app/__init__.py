import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

from .auth import auth as auth_blueprint
app.register_blueprint(auth_blueprint,url_prefix='/auth')

#Flask-Login
from flask_login import LoginManager
login_manager = LoginManager()
login_manager.login_view = 'auth.login' #告知果到保護的頁面必需到Blueprint.function
login_manager.init_app(app)

@app.route("/")
def index():
    return "Hello!Jenny"