import os
import requests
from . import db

class City(db.Model):
    __tablename__ = "city"
    id = db.Column(db.Integer, primary_key=True)
    cityName = db.Column(db.String(20))
    continent = db.Column(db.String(20))
    country = db.Column(db.String(20))
    description = db.Column(db.Text)
    image = db.Column(db.String)
    lat = db.Column(db.Float)
    lon = db.Column(db.Float)
    url = db.Column(db.String)

    def __repr__(self):
        return f"<City cityName={self.cityName}>"

def createDB():
    basedir = os.path.abspath(os.path.dirname(__file__))
    sqlitePath = os.path.join(basedir,'cities.sqlite')
    if not os.path.exists(sqlitePath):
        print("下載資料")
        response = requests.get('https://flask-robert.herokuapp.com/city')
        allData=response.json()
        allCity = allData['allCity']
        for city in allCity:
            print(city)
            print("==========")
        #db.create_all()
    else:
        print('已經建立')

