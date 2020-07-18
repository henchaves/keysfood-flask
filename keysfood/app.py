from flask import Flask

from keysfood.ext import site
from keysfood.ext import toolbar
from keysfood.ext import config
from keysfood.ext import db
from keysfood.ext import cli
from keysfood.ext import migrate
from keysfood.ext import hooks
from keysfood.ext import auth
from keysfood.ext import admin



def create_app():
    app = Flask(__name__)
    
    config.init_app(app)
    db.init_app(app)
    auth.init_app(app)
    admin.init_app(app)
    migrate.init_app(app)
    cli.init_app(app)
    toolbar.init_app(app)
    site.init_app(app)
    hooks.init_app(app)

    return app

