from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField
from wtforms.validators import DataRequired

class NameForm(FlaskForm):
    name = StringField("您的姓名是?", validators=[DataRequired()])
    submit = SubmitField('Submit')