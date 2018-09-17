from flask import Flask

app = Flask(__name__)

from dtblog.core.views import core
from dtblog.error_pages.handlers import error_pages

app.register_blueprint(core)
app.register_blueprint(error_pages)
