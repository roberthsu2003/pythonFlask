from flask import Flask,render_template
import plotly.express as px
import plotly
import json


app = Flask(__name__)

@app.route("/")
def hello_world():
    df = px.data.tips()
    fig = px.scatter(df, x="total_bill", y="tip", trendline="ols")
    graphJSON = json.dumps(fig,cls=plotly.utils.PlotlyJSONEncoder)

    return render_template('index.jinja.html',graphJSON=graphJSON)