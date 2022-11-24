from flask import Flask,render_template

app = Flask(__name__)

@app.route('/')
def index():
    #flask基本建構教學
    #基本網網頁套用css語法
    return render_template('sample1/index.html')