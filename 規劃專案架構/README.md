# 規劃專案架構
制作簡單的網站，或許一個應用程式檔案就可以了，但這樣這網站就不容易擴充，這個應用程式內的程式碼也會非常的多和複雜。


## 一個最簡單專案
```
|-project/
	|-app/
		|-templates/
		|-static
		root.py
		form.py
		models.py
```

### root.py

```python
from flask import Flask


app = Flask(__name__)
@app.route('/',methods=['GET'])
def index():
    return '<h1>Hello! Flask</h1>'
    
@app.route('/login',methods=['GET'])
def login():
    return '<h1>登入頁面</h1>'

@app.errorhandler(404)
def page_not_found(e):
    return "<h1>沒有發現網頁</h>",404

if __name__ == "__main__":
    app.run(debug=True)e)
```

## 當專案愈來愈大時，建立處理login功能和處理錯誤的error module
- 將錯誤功能交給error.py
- 將錯誤功能交給login.py

```
|-project/
	|-app/
		|-templates/
		|-static/
		root.py
		login.py
		error.py
		form.py
		models.py
```

### 將error功能交給error.py

#### root.py

```python
from flask import Flask
import errors

app = Flask(__name__)
@app.route('/',methods=['GET'])
def index():
    return '<h1>Hello! Flask</h1>'

@app.route('/login',methods=['GET'])
def login():
    return '<h1>登入頁面</h1>'

```


#### error.py

```python
from root import app
@app.errorhandler(404)
def page_not_found(e):
    return "<h1>沒有發現網頁</h>",404
```

#### flask run時發生circular錯誤

```
ImportError: cannot import name 'app' from partially initialized module 'root' (most likely due to a circular import) 
```

> 原因在

> root.py內import error

> error.py內from root import app

> 互相import導至於無限循環import


#### 解法方法1:
將app透過參數傳至error內

#### root.py

```python
from flask import Flask
import errors

app = Flask(__name__)
errors.init_app(app)

@app.route('/',methods=['GET'])
def index():
    return '<h1>Hello! Flask</h1>'

@app.route('/login',methods=['GET'])
def login():
    return '<h1>登入頁面</h1>'
```

#### error.py

```python
def init_app(app):
    @app.errorhandler(404)
    def page_not_found(e):
        return "<h1>沒有發現網頁</h>", 404
```


#### 解法方法2:使用Blueprint

##### 改變結構

```
|-project/
	|-app/
		|-templates/
		|-static/
		|-login/
			main.py
		|-error/
			main.py
		root.py
		form.py
		models.py
```

##### root.py

```python
from flask import Flask
from errors.main import errors
from login.main import login

app = Flask(__name__)
app.register_blueprint(errors)
app.register_blueprint(login)

@app.route('/',methods=['GET'])
def index():
    return '<h1>Hello! Flask</h1>'

if __name__ == "__main__":
    app.run(debug=True)
```

##### error/main.py

```python
from flask import Blueprint
errors = Blueprint('errors',__name__)


@errors.app_errorhandler(404)
def page_not_found(e):
    return "<h1>沒有發現網頁</h>", 404

```

##### login/main.py

```python
from flask import Blueprint
login = Blueprint('login',__name__)

@login.route('/login', methods=['GET'])

def user_login():
    return "<h1>登入畫面</h1>"

```

#### 解法方法3:使用Blueprint(在login目錄和error目錄建立__init__)

##### 架構

```
|-project/
	|-app/
		|-templates/
		|-static/
		|-login/
			__init__.py
			main.py
		|-error/
			__init__.py
			main.py
		root.py
		form.py
		models.py
```

##### root.py

```python
from flask import Flask
from errors import errors
from login import login

app = Flask(__name__)
app.register_blueprint(errors)
app.register_blueprint(login)

@app.route('/',methods=['GET'])
def index():
    return '<h1>Hello! Flask</h1>'

if __name__ == "__main__":
    app.run(debug=True)
```

##### error目錄__init__.py

```python
from flask import Blueprint
errors = Blueprint('errors',__name__)
from . import main
```

##### error目錄main.py

```python
from . import errors

@errors.app_errorhandler(404)
def page_not_found(e):
    return "<h1>沒有發現網頁</h>", 404

``` 

##### login目錄__init__.py

```python
from flask import Blueprint
login = Blueprint('login',__name__)

from . import main
```

##### login目錄main.py

```python
from . import login

@login.route('/login', methods=['GET'])

def user_login():
    return "<h1>登入畫面</h1>"
```

## Blueprints 進階參數設定

### url_prefix參數

```python
app.register_blueprint(login, url_prefix='/xxx')
```

http://127.0.0.1/xxx/login

### static_folder,template_foler

1. 程式碼修變

```python
errors = Blueprint('errors',__name__,static_folder='static',template_folder='templates')

login = Blueprint('login',__name__,static_folder='static',template_folder='templates')
```

2. 架構更新

```
|-project/
	|-app/
		|-templates/
			|-login/
				index.html
			|-error/
				error.html
		|-static/
			|-login/
				xxx.css
			
		|-login/
			__init__.py
			main.py			
		|-error/
			__init__.py
			main.py			
		root.py
		form.py
		models.py
```

3 templates資料夾的呼叫

```python
#root.py
render_template('index.html')

#login/main.py
render_template("login/index.html")

#error/main.py
render_template('errors/index.html')
```

4 static資料夾的呼叫

```
#templates/index.html
{{ url_for('static',filename='Akihabara.jpg')}}

#templates/errors/index.html
{{ url_for('static',filename='errors/Berlin.jpg')}}

#templates/login/index.html
{{ url_for('static',filename='login/Chiba.jpg')}}
```

5 連結

```
#templates/index.html
{{url_for('login.user_login')}}

#templates/login/index.html
{{ url_for('index')}}
```


建立一個應用程式的專案就需要規畫專案的架構

```
|-project/
	|-app/
		|-templates/
		|-static/
		|-main/
			|-__init__py
			|-errors.py
			|-forms.py
			|-views.py
		|-__init__.py
		|-email.py
		|-models.py
	|-migrations/
	|-tests/
	|-venv/
	|-requirements.txt
	|-config.py
	|-project.py
```

### 建立4個目錄主要架構
- app 

		所有的Flask應用程式皆儲存在這裏，並且成為一個package，所以加入了__init__.py檔
	
- migrations

		包函資料庫所有遷移的描素檔

- test

		 網站測試是一個package

- venv 

		python的模擬環境
		
### 檔案
- requirements.txt

		所有應用到的套件名稱都寫在此處，有利於未來在不同電腦時，要建立相同的模擬環境
		
- config.py 

		儲存所有的設定內容
		
- project.py

		建立Flask應用程式，還有一些管理應用程式的任務

## 專案的設定

一個應用程	式的開發會用到非常多的設定，特別是在不同的環境下可能要使用到不同的設定，例如開發中時的設定，測試時的設定，還有真正發佈時的設定，每一種都有不同的設定檔，所以建立一個config.py檔可動態改變環境設定的方式，就非常重要。

取代原來在主應用程式中使用app.config的方式，取而代之的是使用config.py, 然後使用主應用程式import這一個config

```python
import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or "hard to guess string"
    MAIL_SERVER = os.environ.get('MAIL_SERVER','smtp.googlemail.com')
    MAIL_PORT = int(os.environ.get('MAIL_PORT','587'))
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS', 'true').lower() in ['true','on','1']
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    FLASKY_MAIL_SUBJECT_PREFIX = '[Flasky]'
    FLASKY_MAIL_SENDER = 'Flasky admin <flasky@example.com>'
    FLASKY_ADMIN = os.environ.get('FLASKY_ADMIN')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    @staticmethod
    def init_app(app):
        pass

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'data-dev.sqlite')

class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or 'sqlite://'

class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'data.sqlite')

config = {
    'development': DevelopmentConfig,
    'testing':TestingConfig,
    'production':ProductionConfig,
    'default':DevelopmentConfig
}
```

上面的程式就是建立一個config的module,裏面建一個baseclass Config,Config內用到所有會開發時使用的設定，再利用繼承的方式，建立不同class,每個class有定義不同開發環境的設定。


## 應用程式套件

app目錄應用程式套件，套件內有所有的應用程式，templates和static目錄也建在裏面，資料庫要使用的models.py和email.py也移到此處

## 建立應用程式製造者

如果使用先前的方式，建立的應用程式是非常方便，但有一個大缺點，應用程式它是被建立在全域環境，其它的套件沒辦法import app來使用，還有就是無法動態的使用環境的設定。

解決的方法就是建立一個factory function, 它是專門建立應用程式的function, 將這個factory function建立在app套件內的__init__.py內。

```python
from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_mail import Mail
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy
from config import config

bootstrap = Bootstrap()
mail = Mail()
moment = Moment()
db = SQLAlchemy

def create_app(config_name):
    app=Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    bootstrap.init_app(app)
    mail.init_app(app)
    moment.init_app(app)
    db.init_app(app)

    #路由和錯誤內容寫這裏
    return app
```










