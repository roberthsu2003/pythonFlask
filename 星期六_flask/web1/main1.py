from flask import Flask
from flask import jsonify
import dataSource

app = Flask(__name__)

@app.route("/")
def index():
    country_list = dataSource.get_countries()
    return jsonify(country_list), 200

if __name__ == "__main__":
    app.run(debug=True)