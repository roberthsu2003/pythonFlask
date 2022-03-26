from flask import Flask
from flask import jsonify
import dataSource

app = Flask(__name__)

@app.route('/')
def index():
    return 'Index Page'

@app.route("/weather")
def show_weather():
    weatherList = dataSource.get_weather_of_taiwan()
    return jsonify(weatherList)

if __name__ == "__main__":
    app.run(debug=True)