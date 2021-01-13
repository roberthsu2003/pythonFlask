# 網頁表單

- 安裝Flask-WTF套件

```
(venv) $ pip install flask-wtf
```

## 設定環境

不像其它的套件，Flask-WTF不需要在應用程式階段初始化，但它需要一個secret key, 這個secret key是一串自定的字串，這字串的目的是保護使用者資料的安全性和完整性。

設定方式如下:

```python
app = Flask(__name__)
app.config['SECRET_KEY'] = '不好猜的文字'
```


app.config是個dictionary，目的是為了儲存整個app的設定，更改內容來達到設定整個網站的目的。

這個環境調整變數也可以儲存成為檔案，利用專用的方法將設定檔載入

> 注意:

> secret_key標準和安全的方式是儲存在環境變數內，而不是放在程式碼中，後面將會討論


## Fomr 類別
使用Flask-WTF, 每一個web form的形成是透過一個繼承於FlaskForm的類別。這個類別內定義所有表單所需要的表單欄位，每一個欄位都有各自的對應物件，每一個欄位都有一個validator參數,這個參數的值必需是一個list,list內要放所需要的function，function是用來驗證使用者輸入的內容是否合法。

建立一個繼承於FlaskForm的NameForm類別，並加入文字欄位和傳出按鈕

```
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField
from wtforms.validators import DataRequired

class NameForm(FlaskForm):
    name = StringField("您的姓名是?", validators=[DataRequired()])
    submit = SubmitField('Submit')
```

name和submit是類別屬性

DataRequired()是檢查使用者在這欄位上必需要填入任何值，不可以是空的。

以下表單是WTForms 對應標準的HTML欄位 

| 欄位類型 | 說明 |
|:--|:--|
| BooleanField | 檢查欄位只接受True和False值 |
| DateField | 文字日期欄位，使用特定格式，接受datetime.date值 |
| DateTimeField | 文字日期時間欄位，使用特定格式，接受datetime.datetime值 |
| DecimalField | 文字欄位接受decimal.Decimal值 |
| FileField | 檔案上傳欄位 |
| HiddenField | 隱藏文字欄位 |
| MultipleFileField | 多個檔案上傳欄位 |
| FieldList | 一組列表的特定格式欄位 |
| FloatField | 文字欄位接受浮點數值 |
| FormField | 表單欄位，放在父表單內 |
| Integer | 文字欄位接受整數數值 |
| PasswordField | 密碼欄位 |
| RadioField | 一組單選鈕 |
| SelectField | 下接式表單 |
| SelectMultipleField | 下接式表單和多選功能 |
| SubmitField | 表單送出資料鈕 |
| StringField | 輸入單行字串欄位 |
| TextAreaField | 多行文字欄位 |

以上是WTForms 的驗證功能

| 驗證功能 | 說明 |
|:--|:--|
| DataRequired | 必需要有資料, 送出時驗證 |
| Email | 驗證email的格式 |
| EqualTo | 比較2個欄位的輸入內容必需相等，用在類似密碼輸入2次 |
| InputRequired | 必需要有資料, 未送出時驗證 |
| IPAddress | IPv4網址驗證 |
| Length | 字串長度的驗證 |
| MacAddress | MAC網址的驗證 |
| NumberRange | 數值範圍的驗證 |
| Optional | 允許欄位為空值 |
| Regexp | 允許自訂文字正規則格式驗證 |
| URL | 驗證網址的格式 |
| UUID | 驗證身份証的格式 |
| AnyOf | 驗證在一組值內，必需有其中一個值 |
| NoneOf | 驗證在一組值內，必需輸入值沒有一個包含在這一組值內|

## 產生HTML的表單

透過viewFunction,傳遞NameForm的實體給樣板，樣板接收到NameForm後，取出類別屬性(就是取出欄位實體)

以下是在樣板內，使用NameForm實體form,取出欄位實體

```
<form method="POST">
	{{ form.hidden_tag() }}
	{{ form.name.label }} {{ form.name() }}
	{{ form.submit() }}
</form>
```

> 注意:
>
> form.hidden_tag()，會產生額外的隱藏欄位，這個隱藏欄位是為了預防CSRF(Cross Site Request Forgery)的詐騙行為

在產生表單欄位時，可以加入一些額外的引數，來增加我們的Html的元素的屬性，例如id,class，以便給javascript或css使用

```
<form method="POST">
	{{ form.hidden_tag() }}
	{{ form.name.label }} {{ form.name(id='my-text-field') }}
	{{ form.submit() }}
</form>
```

使用Flask-Bootstrap樣板, Flask-Bootstrap也有支援Flask-WTF，使用Flask_Bootstrap的quick_form()建立支援Flask_WTF的Bootstrap表單。

```
{% import "bootstrap/wtf.html" as wtf %}
{{ wtf.quick_form(form) }}
```

下面是完整的網頁頁面
```{% extends "base.html" %}
{% import "bootstrap/wtf.html" as wtf %}
{% block title %} Flask_Robert {% endblock %}
{% block page_content %}
<div class="page-header">
 <h1>Hello, {% if name %}{{name}}{% else %}Stranger{% endif %}!</h1>
</div>
{{wtf.quick_form(form)}}
{% endblock %}
```

## View Function處理表單

```python
from hello import NameForm


app = Flask(__name__)
app.config['SECRET_KEY'] = 'security code'
bootstrap = Bootstrap(app)
moment = Moment(app)

@app.route('/', methods=['GET', 'POST'])
def index():
    name = None
    form = NameForm()
    if form.validate_on_submit():
        name = form.name.data
        form.name.data = ''
    return render_template('index.html', form=form, name=name)


@app.route('/user/<name>')
def user(name):
    return render_template('user.html',name=name)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500
    
```

form.validate_on_submit()，如果表單已經送出則傳出True,如果表單尚未傳出，則傳出False