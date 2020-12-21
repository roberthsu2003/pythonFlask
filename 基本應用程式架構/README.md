# 基本應用程式架構
## 初始化應用程式

```python
from flask import Flask
app = Flask(__name__)
```

## 規畫路徑

```python
from flask import Flask
app = Flask(__name__)


@app.route('/')
def index():
    return '<h1>Hello Flask! </h1>'
```

## 規畫動態路徑

```python
@app.route('/user/<name>')
def user(name):
	return '<h1>Hello, {}!</h1>'.format(name)
```

## 啟動應用程式

```
#macOS,Linux
$ export FLASK_APP=lesson1.py 
$ flask run

結果:==========================
 * Serving Flask app "./code/lesson1.py"
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)

```

```
#windows
$ set FLASK_APP=lesson1.py 
$ flask run

結果:=============================
 * Serving Flask app "./code/lesson1.py"
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)

```

### 檢視首頁

![](./images/pic1.png)

### 檢視動態路徑

![](./images/pic2.png)





