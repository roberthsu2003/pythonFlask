from flask import render_template,redirect,request,url_for,flash
from flask_login import login_user, login_required, logout_user
from . import auth
from .forms import LoginForm,RegistrationForm
from ..models import User,db
from .. import login_manager

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@auth.route('/login',methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        print('user',user)
        if user is not None and user.verify_password(form.password.data):
            login_user(user, form.remember_me.data)
            next = request.args.get('next')
            if next is None or not next.startswith('/'):
                next = url_for('index')
            return redirect(next)
        flash("不合法的使用者和密碼")
    return render_template('auth/login.html',form=form)

@auth.route('/logout')
@login_required
def logout():
    login_user()
    flash("You have been logged out.")
    return redirect(url_for('index'))

@auth.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(email=form.email.data,
                    username=form.username.data,
                    password=form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('You can now login.')
        return redirect(url_for('auth.login'))
    return render_template('auth/register.html', form=form)

