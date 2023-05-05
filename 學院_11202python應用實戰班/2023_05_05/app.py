from flask import Flask,render_template

app = Flask(__name__)
@app.route("/")
def index():
    data = {
        "key1":'''台股受台積電、航運股跌勢拖累，今 (3) 日開盤下挫，早盤一度跌逾百點，儘管尾盤跌勢收斂，終場仍下跌 83.07 點，或 0.53% 至 15553.41 點，再度失守季線，成交量 2013.79 億元。''',
        "key2":'''電金權值股中，台積電失守 500 元關卡，下跌 1%，聯發科逆勢上漲 1.3%，日月光也走強上漲 1%，不過航運股今日跌勢兇猛，長榮下挫 3.54%、萬海 4.27%、陽明跌 1.94%。''',
        "key3":'''高價股今日表現疲軟，祥碩下跌 3.9%、緯穎、世芯 - KY 下跌超過 2%，信驊、亞德客 - KY、創意下跌超過 1%，大立光、力旺、譜瑞 - KY 小漲作收，保瑞上漲 1% 以上。'''
    }
        
    return render_template("index.jinja.html",content_data=data)

@app.route("/learning/")
def learning():
    return render_template("learning.jinja.html")
