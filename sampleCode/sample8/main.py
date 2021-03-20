from flask import Flask,jsonify,render_template
from flask_bootstrap import Bootstrap
import datasource
import gjun
import os
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
bootstrap = Bootstrap(app)
app.config['JSON_AS_ASCII'] = False
basePath = os.path.abspath(os.path.dirname(__file__))
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


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/youbike/',methods=['GET'])
def get_areas():
    return jsonify({
        'areas':datasource.areas
                    })

@app.route('/youbike/<areaName>',methods=['GET'])
def get_simpleData(areaName):
    simpleData = datasource.getAreaSimpleInfo(areaName)
    if simpleData:
        return jsonify({'data':simpleData})
    else:
        return jsonify({'data':'error'}), 404


@app.route('/gjun',methods=['GET'])
def get_allStation():
    return jsonify(gjun.json)

@app.route('/city',methods=['GET'])
def get_allCity():
    jsonList = []
    cityList = City.query.all()
    for cityObj in cityList:
        city = {}
        city['id'] = cityObj.id
        city['cityName'] = cityObj.cityName
        city['continent'] = cityObj.continent
        city['country'] = cityObj.country
        city['image'] = "https://flask-robert.herokuapp.com/static/cityImage/" + cityObj.image
        city['description'] = cityObj.description
        city['lat'] = cityObj.lat
        city['lon'] = cityObj.lon
        city['url'] = cityObj.url
        jsonList.append(city)
    return jsonify({'allCity':jsonList})
