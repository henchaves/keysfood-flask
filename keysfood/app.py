from flask import Flask

from keysfood.ext import site
from keysfood.ext import toolbar
from keysfood.ext import config


def create_app():
    app = Flask(__name__)
    
    config.init_app(app)
    toolbar.init_app(app)
    site.init_app(app)

    return app

