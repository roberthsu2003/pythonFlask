# 資料庫

應用程式的資料庫，主要功能當然是儲存資料，也可以依據需求取出對應的資料。目前比較普遍在使用的稱為關聯式資料庫，並且使用的語言稱為Structured Query Language.最近也有較新類型的資料庫，如以文件為導向的(document-oriented),keyValueb為導向(key-value)資料庫，統稱為NOSQL，意思是說存取資料庫將不再使用SQL語法。

## 使用Flask-SQLAlchemy操控資料庫
Flask-SQLAlchemy是一個可用於Flask內的套件，它專門可以使用MySQL,Postgres,SQLite。

Flask-SQLAlchemy提供外部為物件導向(ORM)語法, 底層為SQL存取資料庫原始功能

### 安裝Flask-SQLAlchemy

```
(venv) pip install flask-sqlalchemy
```

Flask-SQLAlchemy database URLs

| 資料庫引擎 | URL |
|:--|:--|
| MySQL | mysql://username:password@hostname/database |
| Postgres | postgresql://username:password@hostname/database |
| SQLite (Linux, macOS) | sqlite:////absolute/path/to/database |
| SQLite (Windows)| sqlite:///c:/absolute/path/to/database |

SQLite資料庫不是一個伺服器，所以不需要有hostname,username和password，而MySQL和Postgres則必需提供。

如果是使用MySQL和Postgres則不一定要建立於本地端，也可以建立在遠端網路

使用SQLAlchemy的第一個動作就是必需在應用程式中先設定這些URL,使用'SQLALCHEMY_DATABASE_URI'

```python
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir,'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

```

## Model定義

由於使用的是ORM，必需一開始定義Model, 一個python的類別對應到一個資料表，類別屬性對應到資料表欄位。

- flask-SQLAlchemy有提供base class建立表格
- flask-SQLAlchemy有提供db.Column()建立欄位


```
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir,'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)

    def __repr__(self):
        return '<Role %r>' % self.name

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, index=True)

    def __repr__(self):
        return '<User %r>' % self.username
```

SQLAlchemy column types

| 類型名稱 | python類型 | 說明 |
|:--|:--|:--|
| Integer | int | 32bits整數 |
| SmallInteger | int  | 16bits整數 |
| BigInteger | int | 沒有限制大小 |
| Float | float | 浮點數 |
| Numeric | decimal.Decimal | 固定點數浮點數 |
| String | str | 可變動長度字串 |
| Text | str | 可變動長度字串, 沒有限定長度 |
| Unicode | unicode | 可變動長度Unicode |
| UnicodeText | unicode | 可變動長度Unicode, 沒有限定長度 |
| Boolean | bool | Boolean value |
| Date | datetime.date | 日期 |
| Time | datetime.time | 時間 |
| DateTime | datetime.datetime | 日期時間 |
| Interval | datetime.timedelta | 一段時間 |
| Enum | str | 字串列表值 |
| PickleType | python任何物件 | Automatic Pickle serialization |
| LargeBinary | str | Binary blob |

SQLAlchemy 欄位選項

| 欄位名稱 | 說明 |
|:--|:--|
| primary_key | True,代表是primary key |
| unique | True,代表數值不可以重覆 |
| index |  True,代表建立欄位索引,搜尋此欄將更有效率|
| nullable | False,代表不可以是空的 |
| default |  定義一個default值|

## 表格間的關聯




