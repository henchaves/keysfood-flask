from flask_migrate import Migrate
from keysfood.ext.db import models, db

migrate = Migrate()

def init_app(app):
  migrate.init_app(app, db)