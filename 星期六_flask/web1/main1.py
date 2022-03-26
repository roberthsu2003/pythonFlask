from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "<H1>Hello world</H1>"

if __name__ == "__main__":
    app.run(debug=True)