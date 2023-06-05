from . import api1

@api1.route("/error")
def error():
    return "處理錯誤"