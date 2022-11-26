from flask import Flask,render_template

app = Flask(__name__)

@app.route('/')
def index():
    #typography, textual
    return render_template('sample1/index1.html')

@app.route('/image')
def image():
    #image
    return render_template('sample1/image.html')

@app.route('/table')
def table():
    #table
    return render_template('sample1/table.html')