from flask import Flask,jsonify,render_template
from flask_bootstrap import Bootstrap
import datasource
app = Flask(__name__)
bootstrap = Bootstrap(app)
app.config['JSON_AS_ASCII'] = False

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