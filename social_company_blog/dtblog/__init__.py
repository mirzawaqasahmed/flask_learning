###############
# imports for the app
###############
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
###############
#app instanciation
###############
app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecret'


################
# database setup
#################
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False

db = SQLAlchemy(app)
Migrate(app,db)

################
# Login Manager
#################
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'users.login'


########################
# import blueprints from the views
#########################
from dtblog.core.views import core
from dtblog.error_pages.handlers import error_pages
from dtblog.users.views import users

########################
# register views to the app
#########################
app.register_blueprint(core)
app.register_blueprint(users)
app.register_blueprint(error_pages)
