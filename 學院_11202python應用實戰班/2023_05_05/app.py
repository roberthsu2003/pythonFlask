from flask import Flask,render_template
import pandas_datareader.data as pdr
import yfinance as yf

app = Flask(__name__)
@app.route("/")
def index():
    yf.pdr_override()
    tw_2303 = pdr.get_data_yahoo('2303.TW')
    series_2303 = tw_2303['Adj Close']
    return render_template("index.jinja.html",stock2303=series_2303)


@app.route("/features/")
def features():
    
    return render_template("features.jinja.html")

@app.route("/priceing/")
def priceing():
    
    return render_template("priceing.jinja.html")

@app.route("/about/")
def about():
    return render_template("about.jinja.html")





    
