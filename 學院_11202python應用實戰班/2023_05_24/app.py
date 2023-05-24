from flask import Flask,render_template
import plotly.express as px
import plotly
import json


app = Flask(__name__)

@app.route("/")
def index():
    df = px.data.tips()
    fig = px.scatter(df, x="total_bill", y="tip", trendline="ols")
    graphJSON = json.dumps(fig,cls=plotly.utils.PlotlyJSONEncoder)

    return render_template('index.jinja.html',graphJSON=graphJSON)

@app.route("/index1")
def index1():
    df = px.data.tips()
    fig = px.scatter(df, x="total_bill", y="tip", trendline="ols")
    graphJSON = json.dumps(fig,cls=plotly.utils.PlotlyJSONEncoder)

    return render_template('index1.jinja.html',graphJSON=graphJSON)

@app.route("/index2")
def index2():
    df = px.data.tips()
    fig = px.scatter(df, x="total_bill", y="tip", trendline="ols")
    graphJSON = json.dumps(fig,cls=plotly.utils.PlotlyJSONEncoder)

    return render_template('index2.jinja.html',graphJSON=graphJSON)