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

from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField
from wtforms.validators import DataRequired
class NameForm(FlaskForm):
    name = StringField("姓名", validators=[DataRequired()])
    submit = SubmitField("送出")


@form.route("/validate",methods=["GET","POST"])
def validate():
    name = None
    form = NameForm()
    if form.validate_on_submit():
        name = form.name.data
    return render_template('/form/validate.html',form=form,name=name),200


