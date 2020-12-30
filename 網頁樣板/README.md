# 網頁樣板
## Jinja2 Template 引擎
樣板必需被建立在templates目錄

1.建立templates/index.html  

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Hello! World!</title>
</head>
<body>
<h1>Hello World!</h1>
</body>
</html>
```

2.建立templates/user.html 

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
<h1>Hello, {{ name }}!</h1>
</body>
</html>
```

3.產生樣板

Flask 提供 render_template() function,以整合janja2樣板引擎。render_template()有2個參數，第一個必需是樣板的檔案名，第2個以後必需是一對的組合，使用方式為引數名稱=值，引數名稱將會成為樣板檔案中的變數，以這個範例，name引數名稱將會為user.html內的name變數。

```python
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/user/<name>')
def user(name):
    return render_template('user.html',name=name)
```

