from . import api1

@api1.route("/stockCode")
def stockCode():
    return "stockCode"