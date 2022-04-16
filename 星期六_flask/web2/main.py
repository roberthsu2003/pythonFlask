from flask import Flask,render_template
import dataSource


app = Flask(__name__)
@app.route("/")
def index():
    conn = dataSource.create_connection('lot.db')
    if conn is not None:
        with conn:
            print("connection successful")
            lotList = dataSource.getlot(conn)
            print(lotList)
    return render_template("a2.html",lotList=lotList)

@app.route("/a3/")
def index1():
    return render_template("a3.html")

@app.route("/api/receive/")
def receive():
    return "<h1>收到</h1>"

if __name__ == "__main__":
    app.run(debug=True)