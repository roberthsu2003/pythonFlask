from flask import Flask,render_template

app = Flask(__name__)

@app.route('/')
def index(name='main'):
    return render_template('index.html',name = name)

@app.route('/generic')
def generic(name='generic'):
    return  render_template('generic.html', name = name)

@app.route('/elements')
def elements(name='elements'):
    return  render_template('elements.html', name = name)