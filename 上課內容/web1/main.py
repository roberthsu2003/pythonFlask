from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return "Hello! Flask1111"

if __name__ == "__main__":
    app.run()