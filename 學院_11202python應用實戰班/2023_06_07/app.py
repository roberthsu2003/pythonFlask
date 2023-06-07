from flask import Flask,render_template,request,url_for,redirect,session

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'


@app.route("/")
def index():    
    return render_template('index.jinja.html')

@app.route("/login",methods=['GET', 'POST'])
def login():
    if request.args.get("error") is not None:
        error = request.args.get("error")
    else:
        error = None
    if request.method == 'POST':
        if request.form['email'] == 'robert@gmail.com' and request.form['pwd'] == '12345':
            session['email'] = request.form['email']
            return redirect(url_for('index'))
        else:
            error="密碼錯誤"
            return redirect(url_for('login',error=error))
    
    return render_template('login.jinja.html', error=error)
    

