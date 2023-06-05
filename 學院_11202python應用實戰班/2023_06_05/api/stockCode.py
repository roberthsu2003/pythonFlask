from . import api1
import pandas as pd
from flask import jsonify

@api1.route("/stockCode")
def stockCode():
    code_dataframe = pd.read_csv("api/codeSearch.csv")
    code_dataframe1 =code_dataframe[['code','name']]
    all_list = code_dataframe1.values.tolist()
    python_list = [{item[0]:item[1]} for item in all_list]
    return jsonify(python_list)