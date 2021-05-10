from . import auth
from flask_wtf import FlaskForm
from wtforms.fields import StringField,SubmitField,PasswordField
from wtforms.validators import DataRequired,Email
from flask import render_template,redirect,url_for,session
from ..model import User


class LoginForm(FlaskForm):
    email = StringField("Email:",validators=[DataRequired(),Email()])
    password = PasswordField("密碼:",validators=[DataRequired()])
    submit = SubmitField("送出")

@auth.route('/login',methods=['GET','POST'])
def login():
    loginForm = LoginForm()
    errorMessage = None
    if loginForm.validate_on_submit():
        email=loginForm.email.data
        password = loginForm.password.data
        user=User.query.filter_by(email=email).first()
        if user and user.verify_password(password):
            session["username"] = user.username
            session["know"] = True
            return redirect(url_for('main.index'))
        else:
            session["username"] = None
            session["know"] = False
            errorMessage = "密碼錯誤"
            print(errorMessage)


    return render_template('/auth/login.html',form = loginForm,error=errorMessage),200