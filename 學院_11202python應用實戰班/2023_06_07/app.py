from flask import Flask,render_template,request,url_for,redirect

app = Flask(__name__)
@app.route("/")
def index():    
    return render_template('index.jinja.html')

@app.route("/login",methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['email'] == 'robert@gmail.com' and request.form['pwd'] == '12345':
            return redirect(url_for('index'))
        else:
            error = '密碼不正確'
    
    return render_template('login.jinja.html', error=error)
    

