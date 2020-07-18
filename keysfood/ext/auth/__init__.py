from keysfood.ext.auth import models
from keysfood.ext.auth.commands import list_users, add_user

from keysfood.ext.db import db
from keysfood.ext.auth.admin import UserAdmin
from keysfood.ext.admin import admin
from keysfood.ext.auth.models import User

def init_app(app):
  """INICIALIZAR FLASK SIMPLE LOGIN + JWT"""
  app.cli.command()(list_users)
  app.cli.command()(add_user)

  admin.add_view(UserAdmin(User, db.session))