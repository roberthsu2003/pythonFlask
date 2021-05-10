from . import auth
from flask_wtf import FlaskForm
from wtforms.fields import StringField,SubmitField,PasswordField
from wtforms.validators import DataRequired,Email

class LoginForm(FlaskForm):
    email = StringField("Email:",validators=[DataRequired(),Email()])
    password = PasswordField("密碼:",validators=[DataRequired()])
    submit = SubmitField("送出")

@auth.route('/login',methods=['GET','POST'])
def login():
    loginForm = LoginForm()
    return "<h1>Hello!Login</h1>"