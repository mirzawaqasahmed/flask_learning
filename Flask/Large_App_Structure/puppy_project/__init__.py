##########################################################
###### setup imports
##########################################################
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

##########################################################
###### create app
##########################################################
app = Flask(__name__)

##########################################################
###### create secret key for forms.
##########################################################
app.config['SECRET_KEY'] = 'mysecretkey'

##########################################################
###### setup db
##########################################################
basedir = os.path.abspath(os.path.dirname(__file__))

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
Migrate(app, db)

##########################################################
###### Register Blueprint
##########################################################
from puppy_project.puppies.views import puppies_blueprint
from puppy_project.owners.views import owners_blueprints

app.register_blueprint(owners_blueprints, url_prefix='/owners')
app.register_blueprint(puppies_blueprint, url_prefix='/puppies')
