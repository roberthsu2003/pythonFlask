from . import auth
from flask_wtf import FlaskForm
from wtforms.fields import StringField,SubmitField,PasswordField
from wtforms.validators import DataRequired,Email
from flask import render_template

class LoginForm(FlaskForm):
    email = StringField("Email:",validators=[DataRequired(),Email()])
    password = PasswordField("密碼:",validators=[DataRequired()])
    submit = SubmitField("送出")

@auth.route('/login',methods=['GET','POST'])
def login():
    loginForm = LoginForm()
    return render_template('/auth/login.html',form = loginForm),200