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

## 變數

- 語法:{{ name }}

代表在該位置上使用變數的值。

Jinja2 的變數可以使用非常多不同的資料型態，下方為使用不同資料類型的使用方法

```
<p>使用Dictionary的值: {{ mydict['key'] }}.</p>
<p>使用list的值: {{ mylist[3] }}.</p>
<p>使用變數當作list的索引: {{ mylist[myintvar] }}.</p>
<p>使用物件內的方法: {{ myobj.somemethod() }}.</p>
```

變數的值可以修飾，稱為變數的filter  

語法: Hello, {{ name|capitalize}}

### Jinja2 變數的filters

| filters名稱 | 說明 |
|:--|:--|
| safe | 不使用escaping,預設全部使用esacping |
| capitalize | 第一個字元為大寫，其餘的為小寫 |
| lower | 全部為小寫 |
| upper | 全部為大寫 |
| title | 每個英文字的第一個字是大寫 |
| trim | 清除文字前面和後面的空白 |
| striptags | 清除變數值內的html標籤 |

使用safe filter,則變數內容如果是`<h1>Hello</h1>`將變成`&lt;h1&gt;Hello&lt;/h1&gt;`
> 注意
>
表單的輸入不要使用safe

## 判斷架構

語法:

```
{% if user %}
	Hello,{{ user }}!
{% else %}
	Hello, Stranger!
{% endif %}
```

## 迴圈架構

語法:

```
<ul>
	{% for comment in comments %}
	<li>{{ comment }}</li>
	{% endif %}
</u>
```

### Jinja2支援巨集(Marcos)

語法:

```
{% macro render_comment(comment) %} 
		<li>{{ comment }}</li>
{% endmacro %}

<ul>
	{% for comment in comments %}
     {{ render_comment(comment) }}
	{% endfor %}
</ul>
```

巨集可以單獨儲存在一個html檔案內，下方的範例是marcos初儲存macros.html檔案內,使用import載入

```
{% import 'macros.html' as macros %}
<ul>
    {% for comment in comments %}
	    {{ macros.render_comment(comment) }}
		{% endfor %}
</ul>
```

### include

網頁可以使用組合的方式建立，部份會重覆使用的程式碼可以放在單獨的html檔案內，要使用時，使用include語法載入

```
{% include 'common.html'%}
```

### 繼承

先建立一個base樣版

```
<html>
    <head>
			{% block head %}
				<title>{% block title %}{% endblock %} - My Application</title> 
			{% endblock %}
    </head>
    <body>
        {% block body %}
        {% endblock %}
    </body>
</html>
```

Base樣板內使用block語法，建立可以在衍生樣板內進行覆寫的區域，在上面的範例中，建立3個block,一個為head block ,title block, 一個為body block。 title block 在 head block內。

使用語法extends繼承base樣板，語法如下

```
{% extends "base.html" %}
{% block title %}Index{% endblock %}
{% block head %}
	{{ super() }}
	<style>
	</style>
{% endblock %}

{% block body %} 
	<h1>Hello, World!</h1> 
{% endblock %}
```

## Bootstrap 整合至Flash-Bootstrap

```
$ pip install flask-bootstrap
```

### 使用Flash-Bootstrap範例,修改py檔

```python
from flask import Flask, render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)
bootstrap = Bootstrap(app)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/user/<name>')
def user(name):
    return render_template('user.html',name=name)
```

### 使用Flash-Bootstrap範例,修改templates/user.html

```
{% extends "bootstrap/base.html" %}
{% block title %}Flasky{% endblock %}
{% block navbar %}
<div class="navbar navbar-inverse" role="navigation">
    <div class="container">
        <div class="navbar-header">
            <button type="button" class="navbar-toggle"
                    data-toggle="collapse" data-target=".navbar-collapse">
                <span class="sr-only">Toggle navigation</span>
                <span class="icon-bar"></span>
                <span class="icon-bar"></span>
                <span class="icon-bar"></span>
            </button>
            <a class="navbar-brand" href="/">Flasky</a>
        </div>
        <div class="navbar-collapse collapse">
            <ul class="nav navbar-nav">
                <li><a href="/">Home</a></li>
            </ul>
        </div>
    </div>
</div>
{% endblock %}
{% block content %}
<div class="container">
    <div class="page-header">
        <h1>Hello, {{ name }}!</h1>
    </div>
</div>
{% endblock %}
```

![](./images/pic1.png)

### Flask-Bootstraps 基本的blocks

| block名稱 | 外部Block |
|:--|:--|
| doc |  |
| html | doc |
| html_attribs | doc |
| head | doc |
| body | doc |
| body_attribs | body |
| title | head |
| styles | head |
| metas | head |
| navbar | body |
| content | body |
| scripts | body |

### 增加自訂的css

```
{% block styles %}
{{super()}}
<link rel="stylesheet"
      href="{{url_for('.static', filename='mystyle.css')}}">
{% endblock %}
```

### 增加自訂的javascript

```
{% block scripts %}
<script src="{{url_for('.static', filename='myscripts.js')}}"></script>
{{super()}}
{% endblock %}
```

### 增加html標籤屬性

```
{% block html_attribs %} lang="en"{% endblock %}
```

## 自訂404錯誤頁面