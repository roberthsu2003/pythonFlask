# 基本應用程式架構
## 初始化應用程式
- 所有Flask的應用程式必需建立application的實體
- web server 接收到使用者端的request，全部會傳遞給這個實體，這個動作就是Web Server Gateway Interface(WSGI)
- app是Flask類別的實體

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


### Debug 模式

Flask應用程式可以選擇開啟Debug模式和reloader模式。

reloader模式是在任何的網站的任何內容有被更改並儲存時，Flash會立即重新啟動，保持最新的狀態。

debug 模式是一個網頁工具，有程式有錯誤，直接顯示於網頁上。

開啟debug模式:FLASK_DEBUG=1

![](images/pic3.png)


> 注意
>
> 如果要在程式來啟動debug模式，請使用 app.run(debut=True)

### 命令列說明

```
(venv) $ flask --help

Usage: flask [OPTIONS] COMMAND [ARGS]...

  A general utility script for Flask applications.

  Provides commands from Flask, extensions, and the application. Loads the
  application defined in the FLASK_APP environment variable, or from a
  wsgi.py file. Setting the FLASK_ENV environment variable to 'development'
  will enable debug mode.

    $ export FLASK_APP=hello.py
    $ export FLASK_ENV=development
    $ flask run

Options:
  --version  Show the flask version
  --help     Show this message and exit.

Commands:
  routes  Show the routes for the app.
  run     Run a development server.
  shell   Run a shell in the app context.

```

```
(venv) $ flask run --help

Usage: flask run [OPTIONS]

  Run a local development server.

  This server is for development purposes only. It does not provide the
  stability, security, or performance of production WSGI servers.

  The reloader and debugger are enabled by default if FLASK_ENV=development
  or FLASK_DEBUG=1.

Options:
  -h, --host TEXT                 The interface to bind to.
  -p, --port INTEGER              The port to bind to.
  --cert PATH                     Specify a certificate file to use HTTPS.
  --key FILE                      The key file to use when specifying a
                                  certificate.

  --reload / --no-reload          Enable or disable the reloader. By default
                                  the reloader is active if debug is enabled.

  --debugger / --no-debugger      Enable or disable the debugger. By default
                                  the debugger is active if debug is enabled.

  --eager-loading / --lazy-loader
                                  Enable or disable eager loading. By default
                                  eager loading is enabled if the reloader is
                                  disabled.

  --with-threads / --without-threads
                                  Enable or disable multithreading.
  --extra-files PATH              Extra files that trigger a reload on change.
                                  Multiple paths are separated by ':'.

  --help                          Show this message and exit.

```

```
(venv) $ export FLASK_APP='./code/lesson1.py'
(venv) $ flask run --host 0.0.0.0
 * Serving Flask app "./code/lesson1.py"
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)


```

### Request-Response的流程

Request - 使用者呼叫網頁
Response - Flask回應使用者的Request

#### request物件

當使用者呼叫時，將會有一些物件傳送到view function內, 而最常使用的是request的物件，這是使用者呼叫時 http request 都會封裝在request物件內。

要接受request物件，可以增加view的引數名稱，但為了簡單化，request物件是全域變數，意思是說，我們可以在不增加引數名稱的方式，就可以取得request物件

```python
from flask import Flask
from flask import request
app = Flask(__name__)


@app.route('/')
def index():
    user_agent = request.headers.get('User-Agent')
    return '<p>您的瀏灠器是{}</p>'.format(user_agent)

結果:=================================
您的瀏灠器是Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.2 Safari/605.1.15
```

##### Flask提供的全域物件

| 變數名稱 | 全文 | 說明 |
|:--|:--|:--|
| current_app | Application context | 應用程式物件 |
| g | Application context | 這是一個暫時的物件，每一個request都會產生各自的物件，結束就釋放 |
| request | Request context | 包含所有HTTP request的資訊 |
| session | Request content | 包含session的資訊 |

##### Flask request 物件的屬性或方法

- form
- args
- values
- cookies
- headers
- files
- get_data()
- get_json()
- blueprint
- endpoint
- method
- scheme
- is_secure()
- host
- path
- query_string
- full_path
- url
- base_url
- remote_addr
- environ

##### Request method的綁定
為每一個request註冊，簡化重覆處理request的程式碼
- before_request
- before_first_request
- after_request
- teardown_request

#### 建立Response物件

一個HTTP response最重要的事是，Flask預設傳回的status code是200,代表成功接收request，會成功完成使用者的需求。錯誤的話，要回覆錯誤的status code.

```python
@app.route('/') 
def index():
	return '<h1>Bad Request</h1>', 400 #400代表request 錯誤
```

使用make_response()手動建立response物件

```python
from flask import make_response
@app.route('/') 
def index():
	response = make_response('<h1>This document carries a cookie!</h1>') 
	response.set_cookie('answer', '42')
	return response
```

##### response物件的屬性和方法

- status_code
- headers
- set_cookie()
- delete_cookie()
- content_length
- content_type
- set_data()
- get_data()

##### 特別的response物件 redirect

```python
from flask import redirect
@app.route('/') 
	def index():
	return redirect('http://www.example.com')
```

#### 特別的response物件 abort

```python
from flask import abort
@app.route('/user/<id>') 
def get_user(id):
	user = load_user(id) 
	if not user:
		abort(404)
	return '<h1>Hello, {}</h1>'.format(user.name)
```

abort()不能傳回，abort()會丟出一個exception



