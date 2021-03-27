# 使用者認證

一般的應用程式會有認證機制，以便於了解使用者是誰?並且讓應用程式針對這個人有適當的回應

## Flask認證擴充程式

python有非常多好的認證擴充程式，但沒有一個可以做到所有的認證功能，所以必需整合部份的擴充程式，成為一套完整的認證機制。

- Flask-Login:管理使用者的登入和使用者的session
- Werkzeug:密碼的雜湊和驗證
- itsdangerous:加密和驗證

認證機制可以整合到以下的套件

- Flask-Mail:傳送一個驗證用的mail
- Flask-Bootstrap:HTML樣版
- Flask-WTF:網頁表單

## 使用Werkzeuge雜湊密碼

Werkzeuge的安全模組可以完成雜湊密碼的工作。雜湊密碼主要有分為2個階段，建立密碼雜湊和驗證密碼雜湊

雜湊密碼是無法回推成為原慶密碼

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

