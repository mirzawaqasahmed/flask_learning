from flask import Blueprint, render_template, request, redirect, url_for,flash
from puppy_project import db
from puppy_project.models import User
from puppy_project.auth.forms import LoginForm, RegistrationForm
from flask_login import login_user, login_required, logout_user

auth_blueprint = Blueprint('auth', __name__,
                              template_folder='templates/auth')

@auth_blueprint.route('/welcome')
@login_required
def welcome_user():
    return render_template('welcome_user.html')

@auth_blueprint.route('/logout')
@login_required
def logout():
    logout_user()
    flash("You have been logged out!")
    return redirect(url_for('index'))

@auth_blueprint.route('/login', methods=['GET', 'POST'])
def login():

    form = LoginForm()

    if form.validate_on_submit():

        user = User.query.filter_by(email=form.email.data).first()

        if user.check_password(form.password.data) and user is not None:
            login_user(user)
            flash("Logged in successfully!")

            next = request.args.get('next')

            if next == None or not next[0] == '/':
                next = url_for('auth.welcome_user')

            return redirect(next)

    return render_template('login.html', form=form)

@auth_blueprint.route('/register', methods=['GET', 'POST'])
def register():

    form = RegistrationForm()

    if form.validate_on_submit():
        user = User(email = form.email.data,
                    username = form.username.data,
                    password = form.password.data)

        db.session.add(user)
        db.session.commit()
        flash("Thanks for registration!")
        return redirect(url_for('auth.login'))

    return render_template('register.html', form=form)
