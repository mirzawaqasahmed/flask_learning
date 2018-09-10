from puppy_project import db, login_manager # login_manager is a library that manages user login and logout behavior.
from werkzeug.security import generate_password_hash, check_password_hash
# UserMixin allows us to call function such as "is authenticated, is active and get_ID"
from flask_login import UserMixin

# This a built-in decorator that loads the user and helps getting the user_id of the user currently logged in from "User" table.
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

class User(db.Model, UserMixin):

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key = True)
    email = db.Column(db.String(64), unique = True, index = True)
    username = db.Column(db.String(64), unique = True, index = True)
    password_hash = db.Column(db.String(128))

    def __init__(self, email, username, password):
        self.email = email
        self.username = username
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class Puppy(db.Model):

    __tablename__ = 'puppies'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    owner = db.relationship('Owner', backref='puppy', uselist=False)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        # return f"Puppy name: { self.name }, Puppy ID: { self.id }"
        if self.owner:
            return f"Puppy name is { self.name }-ID:{ self.id } and owner is { self.owner.name }"
        else:
            return f"Puppy name is { self.name }-ID:{ self.id } and has no owner yet!"

class Owner(db.Model):

    __tablename__ = 'owners'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text, index=True)
    puppy_id = db.Column(db.Integer, db.ForeignKey('puppies.id'))

    def __init__(self, name, puppy_id):
        self.name = name
        self.puppy_id = puppy_id

    def __repr__(self):
        return f"Owner name: { self.name }, Puppy ID: { self.puppy_id }"
