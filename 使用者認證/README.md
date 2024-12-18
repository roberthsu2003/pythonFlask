# 使用者認證

一般的應用程式會有認證機制，以便於了解使用者是誰?並且讓應用程式針對這個人有適當的回應

## Flask認證擴充程式

python有非常多好的認證擴充程式，但沒有一個可以做到所有的認證功能，所以必需整合部份的擴充程式，成為一套完整的認證機制。

- Flask-Login:管理使用者的登入和使用者的session
- Werkzeug:密碼的雜湊和證明
- itsdangerous:產生安全加密密碼和驗證

認證機制可以整合到以下的套件

- Flask-Mail:傳送一個驗證用的mail
- Flask-Bootstrap:HTML樣版
- Flask-WTF:網頁表單

## 確保使用者密碼安全

大部份使用者的帳號和密碼都被儲在資料庫內，如果不小心被駭客竊取，將會危害到使用者的帳戶安全，不可否認的，現在的使用者在不同的網站所使用的密碼都是同一組密碼。所以確何使用者密碼安全就非常重要。

儲存在資料庫的密碼必需是雜湊密碼，就算密碼被竊，也無法透過雜湊密碼轉換為真實密碼。

## 使用Werkzeuge雜湊密碼

Werkzeuge的安全模組可以完成雜湊密碼的工作。雜湊密碼主要有分為2個階段，建立密碼雜湊和驗證密碼雜湊

雜湊密碼是無法回推成為原始密碼

- 建立雜湊密碼

		generate_password_hash(password, method='pbkdf2:sha256', salt_length=8)
		
	這個function,將一般的密碼文字，透過method指定的運算機制，產生一個雜湊密碼，雜湊密碼將被儲存於資料庫內，使用method和salt_length參數的預設值就足夠應付大部份的需求
	
- 驗證雜湊密碼

		check_password_hash(hash, password)	

這個function, 將是從資料庫取出雜湊密碼並且比對使用者密碼，如果是正確的將會傳回True。

#### project1/app/models.py

```python
class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, index=True)
    password_hash = db.Column(db.String(128),nullable=False)

    @property
    def password(self):
        raise AttributeError('密碼無法讀取')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self,password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return '<User %r>' % self.username
```

### 使用flask shell驗證

```
(venv) $ flask shell
>>> from app.models import User
>>> user1 = User()
>>> user1.username = 'robert'
>>> user1.password
Traceback (most recent call last):
  File "<console>", line 1, in <module>
  File "/Users/roberthsu2003/Documents/GitHub/pythonFlask/使用者認證/project1/app/models.py", line 13, in password
    raise AttributeError('密碼無法讀取')
AttributeError: 密碼無法讀取

>>> user1.password='a1213'
>>> user1.password_hash
'pbkdf2:sha256:150000$6fLPIEMQ$6edc025b8517868be8e1188b002a5539e69f63d94eb6c3a753df52aadacd46de'
>>> user1.verify_password('a1213')
True
>>> user1.verify_password('a4567')
False
>>> user2 = User()
>>> user2.username='jenny'
>>> user2.password = 'a1213'
>>> user2.password_hash
'pbkdf2:sha256:150000$Gdqbp2MA$311ece94314edb033d2b806feb3e6f997ea208f830de0d7613afebc3a0d2b99c'
```

> 相同的密碼,hash是不一樣的

## 建立一個auth Blueprint

### 架構

```
|-project1/
	main.py
	|-app/
		__init__.py
		data.sqlite
		models.py
		|-auth/
			__init__.py
			views.py
		|-templates/
			|-auth/
				login.html
```

### app/auth/__init__.py

```python
from flask import Blueprint
auth = Blueprint('auth',__name__)
from . import views
```

### app/auth/view.py

```python
from flask import render_template
from . import auth

@auth.route('/login')
def login():
    return render_template('auth/login.html')
```

### app/__init__.py

```python
from .auth import auth as auth_blueprint
app.register_blueprint(auth_blueprint,url_prefix='/auth')
```

## 使用Flask-Login認證
當使用者登入至應用程式時，認證的狀態必需被記錄到使用者的session內，以便於使用者導覽至網站內不同的網頁，應用程式依然知道是那一位使用者。

Flask-Login套件，專門是針對帳號密碼驗證工作，方便開發者不需重覆做驗證工作。

```
(venv) $ pip install flask-login
```

### 和User Model共同工作

Flask-Login必需緊密和使用者模組共同工作，要讓Flask-Login正常運作，User Model需增加一些必要的屬性和方法，如下表:

| python/方法 | 說明 |
|:--|:--|
| is_authenticated | True代表使用者合法驗証的登入 |
| is_active | True代表使用者被允許使用登入系統 |
| is_anonymous | True代表使用者是暱名者 |
| get_id() | 傳回使用者的識別id,編碼成為unicode 字串 |

Flask-Login提供UserMixin類別，已經定義好上述的屬性和方法

```python
#app/models.py
#必需增加email欄位
#部份相關程式碼

class User(UserMixin,db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, index=True)
    email = db.Column(db.String(64),unique=True,index=True)
    password_hash = db.Column(db.String(128),nullable=False)
```

### 初始化Flask-login

- login_view - 告知Flask-login的頁面在何處，當使用者至保護頁面，而沒有login，必需導向使用者至這個頁面Blueprint.function
- 
```python
#app/__init__.py

from flask_login import LoginManager
login_manager = LoginManager()
login_manager.login_view = 'auth.login' login_manager.init_app(app)
```

最終必需指定一個function,是當Flask-login需要從資料庫取出使用者的資料。

```python
#app/models.py

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
```

### 保護頁面(需要login)

decorators是可以串接在一起的，下面的程式可以想像同時註冊一個頁面，也同時註冊這個頁面是受保護的。順序不可以相反，會產生錯誤。沒有登入過的使用者將被導向Login頁面。

```python
#app/__init__.py

from flask_login import login_required
@app.route('/secret')
@login_required
def secret():
    return "只有認證通過的使用者可以看到這個頁面"
```

### 增加一個Login-Form

```python
#app/auth/models.py

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Length, Email

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired, Length(1,64),Email])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField("Keep me login in")
    submit = SubmitField("Log In")
```