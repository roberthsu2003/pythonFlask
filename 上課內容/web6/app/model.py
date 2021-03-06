import os
import requests
from . import db
from werkzeug.security import generate_password_hash,check_password_hash

class City(db.Model):
    __tablename__ = "city"
    id = db.Column(db.Integer, primary_key=True)
    cityName = db.Column(db.String(30))
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
        db.create_all()
        response = requests.get('https://flask-robert.herokuapp.com/city')
        allData=response.json()
        allCity = allData['allCity']
        for city in allCity:
            cityObject = City(cityName=city['cityName'],continent=city['continent'],country=city['country'],description=city['description'],image=city['image'],lat=city['lat'],lon=city['lon'],url=city['url'])
            db.session.add(cityObject)
        db.session.commit()

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    passwordHash = db.Column(db.String(128))

    def __repr__(self):
        return f"<User username={self.username}>"

    @property
    def password(self):
        raise AttributeError


    @password.setter
    def password(self,pwd):
        self.passwordHash = generate_password_hash(pwd);

    def verify_password(self, password):
        return check_password_hash(self.passwordHash,password)
