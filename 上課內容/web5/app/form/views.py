from . import form
from flask import render_template,request

@form.route("/",methods=["GET","POST"])
def form1():
        class Person():
            def __init__(self, email=None, desc=None, overnight=None):
                self.email = email
                self.desc = desc
                self.overnight = overnight

        if request.method == "POST":
            email = request.form.get('email')
            desc = request.form.get('desc')
            overnight = request.form.get('overnight')

            p1=Person(email=email, desc=desc, overnight=overnight)
            return render_template("/form/index.html",person=p1), 200
        else:
            return render_template("/form/index.html"), 200

@form.route("/validate",methods=["GET","POST"])
def validate():
    return render_template('/form/validate.html'),200


