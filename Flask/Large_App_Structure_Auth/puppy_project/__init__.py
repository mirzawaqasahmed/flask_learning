##########################################################
###### setup imports
##########################################################
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

##########################################################
###### LoginManager
##########################################################
login_manager = LoginManager()

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

# This is initiating the login manager and we are passing  our app into it.
login_manager.init_app(app)
# In this case we are redirecting the user to "login" view after successful login. So later we have to create the view too.
login_manager.login_view = 'login'
##########################################################
###### Register Blueprint
##########################################################
from puppy_project.puppies.views import puppies_blueprint
from puppy_project.owners.views import owners_blueprint
from puppy_project.auth.views import auth_blueprint

app.register_blueprint(owners_blueprint, url_prefix='/owners')
app.register_blueprint(puppies_blueprint, url_prefix='/puppies')
app.register_blueprint(auth_blueprint, url_prefix='/auth')
