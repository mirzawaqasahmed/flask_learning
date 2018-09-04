import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

#########################################

basedir = os.path.abspath(os.path.dirname(__file__))
# __file__ is built in funtion that grabs the name of the module or file
# that is run. in case it will be db_ex01.py. Then dirname() is going
# to get the directory where the __file__ is locatied. Then abspath()
# is going to get the absolute path of the directory. Essentially giving
# us base directory path of the file being run.

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


# the above block of code will create a database for us.
#########################################

class Puppy(db.Model):

    # this is how you define the table name. it is also defined automatically.
    # but this is how you will customize it.
    __tablename__ = 'puppies'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    age = db.Column(db.Integer)

    def __init__(self, name, age):

        self.name = name
        self.age = age

# this will allow to debug. For instance if you want to print a specific row.
# if you dont set this function you wont have the ability to see it later.
    def __repr__(self):
        return f"Puppy { self.name } is { self.age } year/s old"
