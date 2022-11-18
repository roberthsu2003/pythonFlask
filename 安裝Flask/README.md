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