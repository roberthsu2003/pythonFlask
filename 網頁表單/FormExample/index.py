from flask import Flask,render_template
import os
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config["SECRET_KEY"] = os.urandom(24)

class NameForm(FlaskForm):
    name = StringField("請輸入姓名",validators=[DataRequired()])
    submit = SubmitField("送出")

@app.route("/",methods=["GET","POST"])
def index():
    name   = None
    form = NameForm()
    print(form)
    if form.validate_on_submit():
        name = form.name.data
        form.name.data = ''
    return render_template("form1.html",form=form,name=name)