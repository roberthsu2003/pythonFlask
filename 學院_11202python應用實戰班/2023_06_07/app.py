from flask import Flask,render_template

app = Flask(__name__)
@app.route("/")
def index():    
    return render_template('index.jinja.html')

@app.route("/login",methods=['GET', 'POST'])
def login():
    return render_template('login.jinja.html')

