from flask import Flask,render_template,request,jsonify
import dataSource


app = Flask(__name__)
@app.route("/")
def index():
    conn = dataSource.create_connection()
    if conn is not None:
        with conn:
            print("connection successful")
            lotList = dataSource.getlot(conn)
            print(lotList)
    return render_template("a2.html",lotList=lotList)

@app.route("/a3/")
def index1():
    return render_template("a3.html")

@app.route("/api/receive/",methods=['GET', 'POST'])
def receive():
    if request.method == "POST":
        lotData = request.get_json().get('lotdata')
        if len(lotData) == 9:
            conn = dataSource.create_connection('lot.db')
            if conn is not None:
                with conn:
                    dataSource.insertData(conn,lotData)
        return "<h1>收到(POST)</h1>"
    elif request.method == "GET":
        return "<h1>收到(GET)</h1>"

@app.route("/api/v8/")
def v8():
    conn = dataSource.create_connection('lot.db')
    lotData = dataSource.getlot(conn)
    print(lotData)
    return jsonify(lotData)

if __name__ == "__main__":
    app.run(debug=True)