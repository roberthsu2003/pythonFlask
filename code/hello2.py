from flask import Flask,render_template,session,redirect,url_for,flash
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = '2uyxdedxgjux8jkKUNkkjwesm'
bootstrap = Bootstrap(app)

class NameForm(FlaskForm):
    name = StringField("請輸入姓名?",validators=[DataRequired()])
    submit = SubmitField("提交")

@app.route('/',methods=['GET','POST'])
def index():
    form = NameForm()
    if form.validate_on_submit():
        old_name = session.get('name')
        if old_name is not None and old_name != form.name.data:
            flash('你已經更改了姓名')
        session['name'] = form.name.data
        return redirect(url_for('index'))
    return render_template('index1.html',form=form,name=session.get('name'))