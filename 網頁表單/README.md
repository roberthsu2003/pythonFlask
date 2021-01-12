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

> 注意:

> secret_key標準和安全的方式是儲存在環境變數內，而不是放在程式碼中，後面將會討論

## Fomr 類別