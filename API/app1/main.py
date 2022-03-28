from flask import Flask
from api import api

app = Flask(__name__)
app.register_blueprint(api)

@app.route("/",methods=['GET', 'POST'])
def hello_world():
    return "<h1>Hello Flask</h1>"

if __name__ == "__main__":
    app.run(debug=True)
