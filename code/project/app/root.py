from flask import Flask
from errors import errors
from login import login

app = Flask(__name__)
app.register_blueprint(errors)
app.register_blueprint(login)

@app.route('/',methods=['GET'])
def index():
    return '<h1>Hello! Flask</h1>'

if __name__ == "__main__":
    app.run(debug=True)
