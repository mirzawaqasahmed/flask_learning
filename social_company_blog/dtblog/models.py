from dtblog import db, login_manager
from werkzeug import generate_password_hash, check_password_hash
from flask_login import UserMixin
from datetime import datetime

@login_manager.user_loader
def load_user(user_id):
    return Users.query.get(user_id)

class Users(db.Model, UserMixin):

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key = True)
    profile_image = db.Column(db.String(64), nullable = False, default = 'default_profile.png')
    email = db.Column(db.String(64), unique = True, index = True)
    username = db.Column(db.String(64), unique = True, index = True)
    password_hash = db.Column(db.String(128))

# the backref atribute is creating a link with the BlogPost database model below. This is just a name for referencing the relationship between Users model and BlogPost model. eventurally it would mean that when a user is posting a blog in the BlogPost model we can refer this author attribute to fetch its related User model information from this table.
# BlogPost will have the user
    posts = db.relationship('BlogPost', backref='author', lazy = True)

# Here the password field is the password entered in the form.
    def __init__(self, email, username, password):
        self.email = email
        self.username = username
        self.password_hash = generate_password_hash(password)

# This function will be used in login view to validate password.
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return f"Username {self.username}"

class BlogPost(db.Model):

    # This is the relationship with the User Model for the specific user
    users = db.relationship(Users)

    id= db.Column(db.Integer, primary_key = True)

    # This is the attribute that connects blogpost to the Users model
    # here users is referencing users = db.relationship(Users) that we created above.
    # This means user_id will be equal to id in the Users Model
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable = False)

    date = db.Column(db.DateTime, nullable = False, default = datetime.utcnow)
    title = db.Column(db.String(140), nullable = False)
    text = db.Column(db.Text, nullable = False)

    def __init__(self, title, text, user_id):
        self.title = title
        self.text = text
        self.user_id = user_id

    def __repr__(self):
        return f"Post ID: {self.id} -- Date: {self.date} -- {self.title}"
