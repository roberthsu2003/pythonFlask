from flask import Flask,render_template
import dataSource


app = Flask(__name__)
conn = dataSource.create_connection('lot.db')
if conn is not None:
    with conn:  #自動close動作
        print("連線成功")
        dataSource.insertData(conn,('robert1',35,21,25,5,17,36,43,'2022-04-16 11:18:20'))

@app.route("/")
def index():
    return render_template("a2.html")

@app.route("/a3/")
def index1():
    return render_template("a3.html")

if __name__ == "__main__":
    app.run(debug=True)