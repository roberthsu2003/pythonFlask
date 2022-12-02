from flask import Flask,render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("form1.html")