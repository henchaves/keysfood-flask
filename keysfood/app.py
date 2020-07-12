from flask import Flask

from keysfood.ext import site
from keysfood.ext import toolbar
from keysfood.ext import config
from keysfood.ext import db
from keysfood.ext import cli

def create_app():
    app = Flask(__name__)
    
    config.init_app(app)
    db.init_app(app)
    cli.init_app(app)
    toolbar.init_app(app)
    site.init_app(app)

    return app

