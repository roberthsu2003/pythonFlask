import os
import sqlite3
from flask_sqlalchemy import SQLAlchemy
from main import app


basePath = os.path.abspath(os.path.dirname(__file__))
cityPath = os.path.join(basePath, 'citys.db')
conn = sqlite3.connect(cityPath)
print('開啟資料庫成功')

c = conn.cursor()
cursor = c.execute("select * from city")
print(cursor.__class__)
citys = list(cursor)
print("select 成功")
conn.close()

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basePath,'citys.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class City(db.Model):
    __tablename__ = 'city'
    id = db.Column(db.Integer, primary_key=True)
    cityName = db.Column(db.String(64), unique=True)
    continent = db.Column(db.String(64), nullable=False)
    country = db.Column(db.String(64), nullable=False)
    image = db.Column(db.String(64), nullable=False)
    description = db.Column(db.Text)
    lat = db.Column(db.Float, nullable=False)
    lon = db.Column(db.Float, nullable=False)
    url = db.Column(db.String(256))

def getAllCities():
    cityList = City.query.all()
    print(cityList)







