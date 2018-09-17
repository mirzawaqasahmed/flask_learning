from flask import render_template, url_for, flash, redirect, request, Blueprint
from flask_login import login_user, current_user, logout_user, login_required
from dtblog import db
from dtblog.models import Users, BlogPost
from dtblog.users.forms import RegistrationForm, LoginForm, UpdateUserForm
from dtblog.users.picture_handler import add_profile_pic

users = Blueprint('users', __name__)

# Register View
@users.route('/register', methods = ['GET', 'POST'])
def register():

    form = RegistrationForm()

    if form.validate_on_submit():
        user = Users(email = form.email.data,
                     username = form.username.data,
                     password = form.password.data)

        db.session.add(user)
        db.session.commit()

        flash('Thank you for registering!') # This may be a split second flash due to the redirect below

        return redirect(url_for('users.login'))

    return render_template('register.html', form=form)

# Login View
@users.route('/login', methods = ['GET', 'POST'])
def login():

    form = LoginForm()

    if form.validate_on_submit():

        user = Users.query.filter_by(email = form.email.data).first()

        # check_password is the function in models.py for validating the password hash.
        if user.check_password(form.password.data) and user is not None:
            login_user(user)
            flash('Log in Successful')

            next = request.args.get('next')

            if next == None or not next[0] == '/':
                next = url_for('core.index')

            return redirect(next)

    return render_template('login.html', form = form)

# Logout View
@users.route('/lgoout')
def logout():
    logout_user()

    return redirect(url_for('core.index'))

# Account View
@users.route('/account', methods = ['GET', 'POST'])
@login_required
def account():

    form = UpdateUserForm()

    if form.validate_on_submit():

        if form.picture.data: # this is saying that if the user has uploaded some data in the file field.
            username = current_user.username
            pic = add_profile_pic(form.picture.data, username)
            # grabing the profile image of the user defined in the Users Model
            current_user.profile_image = pic # pic here will be the pic file path on the disk.

        current_user.username = form.username.data
        current_user.email = form.email.data

        db.session.commit()
        flash('User Account Updated!')

        return redirect(url_for('users.account'))

    elif request.method == 'GET': # This is saying that when the user will initially come to the account page (i.e. the request will be get.) then grab the username and password for him and autofil the fields.
        form.username.data = current_user.username
        form.email.data = current_user.email

    # this is loading the profile image
    profile_image = url_for('static', filename = 'profile_pics/' + current_user.profile_image)

    return render_template('account.html', profile_image = profile_image, form = form)

# User account blog posts
@users.route('/<username>')
def user_posts(username):

    page = request.args.get('page', 1, type = int)
    user = Users.query.filter_by(username = username).first_or_404()

    # Here we are requesting all blog posts specific to the user.
    # The way it is done is using the author=user.
    # author is the link b/w Users and BlogPost model.
    # We are querying the BlogPost model and saying grab all the posts
    # where author = user i.e. author is the user we queried in the above line.
    # which in return is the username given in the app.route.
    blog_posts = BlogPost.query.filter_by(author = user).order_by(BlogPost.date.desc()).paginate(page=page, per_page=5)

    return render_template('user_blog_posts.html', blog_posts=blog_posts, user=user)

# All blogpost of users...
