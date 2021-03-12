from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generic')
def second():
    return render_template('generic.html')

@app.route('/elements')
def third():
    return render_template('elements.html')