## 最簡單的表單範例

- 參考flask_wtf的官網

**Flask建立secret key**

```python
import secrets

app = Flask(__name__)
app.config['SECRET_KEY'] = secrets.token_hex(16) 
```

**建立繼承FlaskForm的class**

```python
from flask_wtf import FlaskForm

class MyForm(FlaskForm):
    name = StringField('name',validators=[DataRequired()])
```

**處理@app.route()**
- methos必需要是支援POST
- 建立MyForm實體
- 要有驗証成功的動作(驗証失敗要顯示於原來的網頁)
- 要把表單實體傳送至網頁

```python
@app.route("/pricing", methods=['GET','POST'])
def pricing():
    form = MyForm()
    if form.validate_on_submit():        
        return redirect(url_for('success')) 
    return render_template('pricing.j2',form=form)
```

**實作表單頁面**
- 必需加上驗証錯誤的處理方法

```python
<form method="POST" action="">
    {{form.csrf_token}}
    {{form.name.label}} {{form.name(size=20)}}
    <input type="submit" value="Go">
</form>
{%if form.name.error %}
    <ul class="error">
    {% for error in form.name.errors %}
        <li>{{ error }}</li>
    {% endfor %}
{% endif %}
```

**傳送成功的頁面**

**py檔**

```
@app.route("/success")
def success():
    return "<h1>表單成功傳送</h1>"
```
