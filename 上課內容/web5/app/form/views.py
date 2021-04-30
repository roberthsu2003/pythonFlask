from . import form
from flask import render_template,request

@form.route("/")
def form():
    email = request.args.get('email')
    desc = request.args.get('desc')
    overnight = request.args.get('overnight')

    class Person():
        def __init__(self,email=None,desc=None,overnight=None):
            self.email = email
            self.desc = desc
            self.overnight = overnight

    p1=Person(email=email, desc=desc, overnight=overnight)



    return render_template("/form/index.html",person = p1), 200