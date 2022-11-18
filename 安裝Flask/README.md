## 安裝Flask

-  建立虛擬環境

```
(venv) $ pip install flask
```

### 檢查目前虛擬環境已經安裝的套件

```
$ pip freeze
結果:=========================
click==7.1.2
Flask==1.1.2
itsdangerous==1.1.0
Jinja2==2.11.2
MarkupSafe==1.1.1
Werkzeug==1.0.1
```

### 檢查是否安裝成功

執行下面程式沒有出錯,代表安裝成功

```
$ python
>>> imort flask
>>>
```

### 建構一個最簡單的應用程式

```python
from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello! World!"
```

#### 執行app
- 檔案名稱不可以是flask.py,會衝突
- 被執行檔案名:wsgi應用程式名(module:app)
- 如果應匆程式名稱是app,可以省略
  
```python
$ flask --help  #查詢
$ flask --app  module:app  run

```

#### 在區網公開此網址

```python
$ flask run --help #查詢
$ flask --app module:app run --host=0.0.0.0
```

#### Debug Mode

```python
$flask --help #查詢
$flask --app module:app --debug --host=0.0.0.0
```

#### HTML Escaping
- 避免攻擊(injection attack)
- escape

> 以下程式輸入<script>alert("bed")</script>

```python
from markupsafe import escape

@app.rout("/<name>")

def hello(name):
    return f"Hello, {escape(name)}!"    
```

#### Routing

```python
@app.route('/')
def index():
	return 'Index Page'
	
@app.route('/hello')
def hello()
	return 'Hello, World'
```

#### 變數使用規則

1. 將變數放至route內，變數的語法為<變數名稱>
2. function必需指定參數接收
3. 變數可以自動轉換為指定資料類型,語法為<int:變數名稱>

```python
from markupsafe import escape

@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return f'User {escape(username)}'

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return f'Post {post_id}'

@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    # show the subpath after /path/
    return f'Subpath {escape(subpath)}'
```

|:--|:--|
| string | (default)沒有符號(/) |
|int|正整數|
| float | 正浮點數 |
| path | string,可以包含(/) |
| uuid | UUID字串 |

#### 網址尾部加上斜線的重新導向行為:URL+(/)

```python
@app.route('/projects/') #重新導向至projects目錄,避免使用
def projects():
    return 'The project page'

@app.route('/about')
def about():
    return 'The about page'
```

#### URL 建立者url_for()

- 第1個參數是使用function名稱
- 第2個參數使用key value

```python
from flask import url_for

@app.route('/')
def index():
    return 'index'

@app.route('/login')
def login():
    return 'login'

@app.route('/user/<username>')
def profile(username):
    return f'{username}\'s profile'

with app.test_request_context():
    print(url_for('index'))
    print(url_for('login'))
    print(url_for('login', next='/'))
    print(url_for('profile', username='John Doe'))
```

```
/
/login
/login?next=/
/user/John%20Doe
```
