import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
########## Migrate code ############
from flask_migrate import Migrate # pip install Flask-Migrate
# you would use flask_migrate to modify the base model of the DB
# for instance if your db was created and now you want to add an
# additional column, you would run the migration option.
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

########## Migrate code ############
Migrate(app,db)
# this is where you have connected your db withe migrate object.
# then go to command line and perform rest of the following tasks.
# export FLASK_APP=db_ex01_basic_migrate.py
# source activate flaskenv01
# flask db init (Here "db" is the instanciation of the app in SQLAlchemy above)
# flask db migrate -m "created puppy table"
# flask db upgrade
# Then make changes to the model i.e. add new column etc.
# flask db migrate -m "Added breed column"
# flask db upgrade


########## Migrate code ############

# the above block of code will create a database for us.
#########################################

class Puppy(db.Model):

    # this is how you define the table name. it is also defined automatically.
    # but this is how you will customize it.
    __tablename__ = 'puppies'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    age = db.Column(db.Integer)
    breed = db.Column(db.Text)

    def __init__(self, name, age, breed):

        self.name = name
        self.age = age
        self.breed = breed

# this will allow to debug. For instance if you want to print a specific row.
# if you dont set this function you wont have the ability to see it later.
    def __repr__(self):
        return f"Puppy { self.name } is { self.age } year/s old"
