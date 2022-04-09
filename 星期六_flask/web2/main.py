from flask import Flask,render_template


app = Flask(__name__)

@app.route("/")
def index():
    name = "Robert"
    age = 18
    return render_template("a1.html",name=name,age=age)

if __name__ == "__main__":
    app.run(debug=True)