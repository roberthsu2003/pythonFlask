from flask import Flask,render_template
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")
@app.route("/layout")
def layout():
    return render_template("layout/index.html")

@app.route("/layout/<name>")
def layoutName(name):
    if name == "a1":
        return render_template("layout/a1.html")
    return  render_template("layout/index.html")

if __name__ == "__main__":
    app.debug = True
    app.run()