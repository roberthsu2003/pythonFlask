from . import form
from flask import render_template,request

@form.route("/")
def form():
    email = request.args.get('email')
    desc = request.args.get('desc')

    if email and desc:
        print(email)
        print(desc)
    return render_template("/form/index.html")