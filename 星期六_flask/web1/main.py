from flask import Flask
from markupsafe import escape
import dataSource

app = Flask(__name__)

@app.route('/')
def index():
    return 'Index Page'

@app.route('/hello')
def hello():
    return 'Hello, World'

@app.route('/world')
def world():
    return "<h1>World</h>"

@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return f'使用者是:{escape(username)}'

@app.route("/weather")
def show_weather():
    return dataSource.weather()

if __name__ == "__main__":
    app.run(debug=True)