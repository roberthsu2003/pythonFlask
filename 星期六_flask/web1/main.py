from flask import Flask
from markupsafe import escape
import dataSource

app = Flask(__name__)

@app.route('/')
def index():
    return 'Index Page'

@app.route("/weather")
def show_weather():
    return dataSource.get_weather_of_taiwan()

if __name__ == "__main__":
    app.run(debug=True)