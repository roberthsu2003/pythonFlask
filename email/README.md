# Flask Email
Flask application 具有發送email的能力。

## Flask-Mail
雖然python已經有內建可傳送mail的smtplib套件，但flask-mail套件更適合整合Flask應用程式。

```
(venv) $ pip install flask-mail
```

這個擴充套件會建立Simple Mail Transfer Protocol(SMTP) server,同時可以將email傳遞給此mail server, 並透過mail server發送。如果沒有做特定設定，Flask-Mail會連結到本機電腦的mail server,連結的port為25，但沒有任何驗證機制。

### 以下為SMTP server 可以設定的key

| key | 預設 | 說明 |
|:--|:--|:--|
| MAIL_SERVER | localhost | mail伺服器的名稱或IP address |
| MAIL_PORT | 25 | email伺服器的port |
| MAIL_USE_TLS | False | 啟動 Transport Layer Security(TLS) 安全機制|
| MAIL_USE_SSL | False | 啟動 Secure Sockets Layer (SSL) 安全機制 |
| MAIL_USERNAME | None | Mail使用者帳號 |
| MAIL_PASSWORD | None | Mail使用者密碼 |

在開發階段，比較適合使用外部SMTP伺服器，例如Google Gmail帳戶。

### Flask-Mail因應Google Gmail的設定

```python
import os

app.config['MAIL_SERVER'] = 'smtp.googlemail.com' app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True 
app.config['MAIL_USERNAME'] = os.environ.get('MAIL_USERNAME') app.config['MAIL_PASSWORD'] = os.environ.get('MAIL_PASSWORD')
```

> 注意:使用者帳號和密碼不要直接寫在程式內，由其是上傳至公開環境，要保護一些比較敏感的資訊，必需要將這些敏感的資訊寫至環境變數內

> 由於安全性的理由，Gmail的帳戶被設定為必需使用OAuth2認證機制的伺服器才可以連結。但Flask-Mail並沒有這機制，所以使用時，必需手動至Gmail帳戶內設定Gmail支援標準的SMTP認證。

> 至[Google account setting page](https://myaccount.google.com)內，選取左邊的安全性，並啟動安全性較低的設定。建議再建立一組google帳號

### Flask-Mail的初始化

```
from flask import Flask
from flask_mail import Mail
import os
app = Flask(__name__)
app.config['MAIL_SERVER'] = 'smtp.googlemail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.environ.get('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.environ.get('MAIL_PASSWORD')
mail = Mail(app)
```

#### 2個環境變數設定的方式如下:

```
#linux,max
(venv) $ export MAIL_USERNAME=<Gmail username> 
(venv) $ export MAIL_PASSWORD=<Gmail password>

#window
(venv) $ set MAIL_USERNAME=<Gmail username> 
(venv) $ set MAIL_PASSWORD=<Gmail password>
```

### 使用Python Shell發送email

```
(venv) $ flask shell
>>> from flask_mail import Message
>>> from hello import mail
>>> msg = Message('test email', sender='you@example.com',recipients=['you@example.com'])
>>> msg.body = 'This is the plain text body'
>>> msg.html = 'This is the <b>HTML</b> body'
>>> with app.app_context():
			 mail.send(msg)
```

> 注意您的應用程式必需是開啟的(flask run)

## 將Email整合至應用程式

為發送email時，建立一個自訂的function send_email(),這個function也可以支援Jinja2的樣版

```python
from flask_mail import Message 
from flask import render_template
app.config['FLASKY_MAIL_SUBJECT_PREFIX'] = '[Flasky]'
app.config['FLASKY_MAIL_SENDER'] = 'Flasky Admin <flaskyy@example.com>'

def send_email(to, subject, template, **kwargs):
		msg = Message(app.config['FLASKY_MAIL_SUBJECT_PREFIX'] + subject,sender=app.config['FLASKY_MAIL_SENDER'],recipients=[to])
		msg.body = render_template(template + '.txt', **kwargs)
		msg.html = render_template(template + '.html', **kwargs)
		mail.send(msg)
```

### 整合應用程式和資料庫

```python
# ...
app.config['FLASKY_ADMIN'] = os.environ.get('FLASKY_ADMIN') # ...
@app.route('/', methods=['GET', 'POST'])
def index():
	form = NameForm()
	if form.validate_on_submit():
		user = User.query.filter_by(username=form.name.data).first() 
			if user is None:
				user = User(username=form.name.data)
				db.session.add(user) 
				session['known'] = False
				if app.config['FLASKY_ADMIN']:
                send_email(app.config['FLASKY_ADMIN'], 'New User','mail/new_user', user=user)
			else:
				session['known'] = True
			session['name'] = form.name.data 
			form.name.data = ''
			return redirect(url_for('index'))
	return render_template('index.html', form=form, name=session.get('name'), known=session.get('known', False))
```


### 傳送非同步Email

```python
from threading import Thread
def send_async_email(app, msg): 
		with app.app_context():
				mail.send(msg)
				
def send_email(to, subject, template, **kwargs):
    msg = Message(app.config['FLASKY_MAIL_SUBJECT_PREFIX'] + ' ' + subject,
                  sender=app.config['FLASKY_MAIL_SENDER'], recipients=[to])
    msg.body = render_template(template + '.txt', **kwargs)
    msg.html = render_template(template + '.html', **kwargs)
    thr = Thread(target=send_async_email, args=[app, msg])
    thr.start()
    return thr

```






