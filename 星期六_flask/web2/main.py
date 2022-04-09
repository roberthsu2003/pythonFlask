from flask import Flask,render_template


app = Flask(__name__)

@app.route("/")
def index():
    return render_template("a2.html")

@app.route("/a3/")
def index1():
    return render_template("a3.html")

if __name__ == "__main__":
    app.run(debug=True)