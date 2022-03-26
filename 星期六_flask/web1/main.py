from flask import Flask
from flask import jsonify
from flask import request

import dataSource

app = Flask(__name__)

@app.route('/')
def index():
    return 'Index Page'
authorization = "rdec-key-123-45678-011121314"

@app.route("/weather")
def show_weather():
    authName = request.args.get("Authorization")
    if authName is None:
        print("沒有Authorization")
    else:
        print(f"Authorization:{authName}")

    format = request.args.get("format")
    if format is None:
        print("沒有format")
    else:
        print(f"format:{format}")

    weatherList = dataSource.get_weather_of_taiwan()
    return jsonify(weatherList)

if __name__ == "__main__":
    app.run(debug=True)