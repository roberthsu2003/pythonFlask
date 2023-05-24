from flask import Flask,render_template,request
import datasource


app = Flask(__name__)
@app.route("/",methods=['GET','POST'])
def index():
    rows = datasource.get_stockid()
    if request.method == 'POST':
        stock_name = request.form['stock_name']  #1203-味王
        stock_id = stock_name[:4]
        year =  request.form['year']
        stock_data = datasource.get_stock_data(stockid=stock_id,year=year)        
        return render_template("form.jinja.html",rows=rows,stock_name=stock_name,year=year,data=stock_data)
    
    
    return render_template("form.jinja.html",rows=rows)


@app.route("/features")
def features():
    
    return render_template("features.jinja.html")

@app.route("/priceing")
def priceing():
    
    return render_template("priceing.jinja.html")

@app.route("/about")
def about():
    return render_template("about.jinja.html")

@app.route("/form/",methods=['GET', 'POST'])
def form():
    rows = datasource.get_stockid()
    if request.method == 'POST':
        stock_name = request.form['stock_name']  #1203-味王
        stock_id = stock_name[:4]
        stock_data = datasource.get_stock_data(stockid=stock_id)
        year =  request.form['year']
        return render_template("form.jinja.html",rows=rows,stock_name=stock_name,year=year,data=stock_data)
    
    
    return render_template("form.jinja.html",rows=rows)
    





    
