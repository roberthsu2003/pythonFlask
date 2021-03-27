from flask import Flask,render_template
from .errors import errors
from .login import login

def create_app():
    app = Flask(__name__)
    app.register_blueprint(errors)
    app.register_blueprint(login)

    @app.route('/',methods=['GET'])
    def index():
        return render_template('index.html')

