from . import api1

@api1.route("/youbike")
def youbike():
    return "<h1>Hello! Youbike</h1>"