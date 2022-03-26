from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return """
    <h1>Hello, World!</H1>
    <ul>
    <li>number1</li>
    <li>number2</li>
    <li>number3</li>
    <li>number4</li>
    </ul>
    """

if __name__ == "__main__":
    app.run(debug=True)