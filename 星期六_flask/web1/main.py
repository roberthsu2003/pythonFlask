from flask import Flask,jsonify,request,abort



import dataSource

app = Flask(__name__)

@app.route('/')
def index():
    return 'Index Page'
authorization = "rdec-key-123-45678-011121314"

@app.route("/weather")
def show_weather():
    authName = request.args.get("Authorization")
    format = request.args.get("format")
    if authName is None or format is None:
        abort(401)

    weatherList = dataSource.get_weather_of_taiwan()
    return jsonify(weatherList)

@app.errorhandler(401)
def noAuthorization(error):
    return "<h1><center>沒有合法的認證<center></h1>", 401

@app.errorhandler(404)
def no_page_found(error):
    return "<h1><center>沒有發現網頁<center></h1>", 404

if __name__ == "__main__":
    app.run(debug=True)