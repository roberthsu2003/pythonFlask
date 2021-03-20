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

1對多的關聯 -> 一個角色可以給多個使用者使用

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
    users = db.relationship('User',backref='role')

    def __repr__(self):
        return '<Role %r>' % self.name

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, index=True)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))

    def __repr__(self):
        return '<User %r>' % self.username
```

## 資料庫操作
當model建立完成後，現在可以使用python shell的方式來操控資料庫，要操控資料庫，必需使用flask shell,注意要用flask shell前，必需先設定FLASK_APP環境變數。

```
(venv) flask shell
>>> from hello import db
>>> db.create_all()
```

使用db.create_all()的語法，將在網站根目錄建立data.sqlite的檔案，如果已經有現有的資料庫時，將不會重新建立。

```
>>> db.drop_all()
#將會把所有資料表刪除, 所有資料被刪除

>>> db.create_all()
#重新建立資料表
```

## 新增一筆記錄

```
>>> from hello import Role, User
>>> admin_role = Role(name='Admin')
>>> mod_role = Role(name='Moderator')
>>> user_role = Role(name='User')
>>> user_john = User(username='john', role=admin_role) 
>>> user_susan = User(username='susan', role=user_role) 
>>> user_david = User(username='david', role=user_role)
```

還沒有加入資料

```
>>> print(admin_role.id) None
>>> print(mod_role.id) None
>>> print(user_role.id) None
```

加入session和session commit才加入成功

```
>>> db.session.add(admin_role) 
>>> db.session.add(mod_role) 
>>> db.session.add(user_role) 
>>> db.session.add(user_john) 
>>> db.session.add(user_susan) 
>>> db.session.add(user_david)
#也可以一次加入
>>> db.session.add_all([admin_role, mod_role, user_role,user_john, user_susan, user_david])
```

```
>>> db.session.commit()
```

```
>>> print(admin_role.id) 
1
>>> print(mod_role.id) 
2
>>> print(user_role.id) 
3
```

### 修改資料

```
>>> admin_role.name = 'Administrator' 
>>> db.session.add(admin_role)
>>> db.session.commit()
```

### 刪除資料

```
>>> db.session.delete(mod_role) 
>>> db.session.commit()
```

### 搜尋資料

```
>>> Role.query.all()
[<Role 'Administrator'>, <Role 'User'>]
>>> User.query.all()
[<User 'john'>, <User 'susan'>, <User 'david'>]
```

使用filter_by()

```
>>> User.query.filter_by(role=user_role).all() 
[<User 'susan'>, <User 'david'>]
```

也可以產生SQL語法

```
>>> str(User.query.filter_by(role=user_role))
'SELECT users.id AS users_id, users.username AS users_username, users.role_id AS users_role_id \nFROM users \nWHERE :param_1 = users.role_id'
```

```
>>> user_role = Role.query.filter_by(name='User').first()
```

### 搜尋請求

| 選項 | 說明 |
|:--|:--|
| filter() | 增加一個新的過濾至query,並傳出一個新的query |
| filter_by() | 增加一個新的有指定內容過濾至query,並傳出一個新的query |
| limin() | 傳出指定數量的query |
| offset() | 傳出一個範圍數量的query |
| order_by() | 傳出一個有排序的query |
| group_by() | 傳出一群有相同值的query |

### SQLAlchemy query executors

| 選項 | 說明 |
|:--|:--|
| all() | 傳回list所有搜尋需求 |
| first() | 傳回搜尋需求的第一個值如果沒有傳出None |
| first_or_404() | 傳品搜尋需求，如果沒有資料則取消請求並傳出404error的response |
| get() | 傳回特定的primary key的row,如果沒有,則傳出None |
| get_or_404() | 傳回特定的primary key的row，如果沒有資料則取消請求並傳出404error的response |
| count() | 傳回需求的筆數 |
| paginate() | 傳回包含指定範圍的Pagination物件 |

### 使用關聯的搜尋方法

```
>>> users = user_role.users
>>> users
[<User 'susan'>, <User 'david'>] 
>>> users[0].role
<Role 'User'>
```









