# 部署

在雲端運算時代裡我們已經不用像過去一樣需要自建機房可以使用雲端服務進行部屬，若是你是一個希望專注在應用程式開發上，不太需要管基礎建設的維護的話可以考慮雲端的 PasS 服務，例如：Heroku 就是一個常用來當作部屬的工具（有提供一定的免費的額度）。

## Heroku
一個免費的雲端平台“Heroku”，這個雲端平台一個帳號可以免費建立五個專案，雖然是免費當然也有使用上的限制
1. 免費建立五個專案
2. 依照 dyno 的運行時間計費。本身提供了550小時的額度。通過信用卡認證後則高達1000小時。一個月算31天，且24小時醒著也頂多744小時，完全足夠使用！
3. 30分鐘沒有使用會進入睡眠狀態，之後要開啟需要等待20秒才能運作。
4. 500MB的儲存空間，這空間對開發者開發一些小專案來說夠用了。當然Heroku也提供多種語言的部署環境像是Ruby、Node.js、PHP 、 Go、Python等等。
5. Heroku計算方式是使用dyno, 免費方式是使用free dyno, dyno 1秒可以處理10~50 request
6. 資料庫免費限制1萬筆，最多20個同時連線

## Heroku簡單部署方式

### 1. 註冊Heroku帳號

### 2. 根據不同作業系統安裝 Heroku CLI

### 3. 專案部份:

#### 建立main.py主程式

```python
from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    return f'Hello, Heroku!'
```

#### 建立Procfile檔

 - 如何運行 Web App，在這邊我們使用 gunicorn 這個 WSGI Server。並輸入下面內容

```
# main是主程式的檔名，app是main.py內的實體app
web: gunicorn main:app
```

#### 建立runtime.txt python使用的版本

```
python-3.8.10
```

#### 建立requirements.txt

- Python 套件清單，告訴 Heroku 需要安裝哪些套件（主要有 gunicorn、flask 我們也可以設定需要安裝的版本）

```
gunicorn
flask
```

### 部署至heroku部份:
#### 登入

```
>>> heroku login
```

#### 在專案資料夾下初始化 git

```
>>> git init
```

#### 建立heroku上的app名稱

```
#app名稱可以使用的特殊字元只有 - 
>>> heroku create <appname>
```

#### 設定目前heroku對應的app名稱

```
>>> heroku config:set FLASK_APP=main.py
```

#### 在本端測試

```
>>> heroku local:run main deploy
>>> heroku local
```

#### 透過 $ heroku git:remote 新增 app repo 為遠端repository

```
#查看說明
>>> heroku git -h

#建立remote
#專案名稱是指在heroku上剛建立的app名稱
>>> heroku git:remote -a 專案名稱
```

#### git commit並push

```
# 將所有更動提交到 staging
$ git add .
# 將所有變動 commit 並加上訊息
$ git commit -a -m "第一次commit"
# 推送到遠端
$ git push heroku master
```

#### 查看log

```
>>> heroku logs --tail
```

#### 更新

```
# 將所有更動提交到 staging
$ git add .
# 將所有變動 commit 並加上訊息
$ git commit -a -m "更新內容"
# 推送到遠端
$ git push heroku master
```
