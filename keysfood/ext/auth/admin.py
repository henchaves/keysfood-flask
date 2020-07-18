from flask_admin.contrib.sqla import ModelView
from flask_admin.actions import action
from keysfood.ext.auth.models import User
from keysfood.ext.db import db
from flask import flash, Markup #Marktup serve para renderizar html

def format_user(self, request, user, *args):
  return user.email.split("@")[0]

class UserAdmin(ModelView):
  """Interface admin de User"""

  column_formatters = {"email": format_user}
  #column_formatters = lambda s, r, u, *a: u.email.split("@")[0]

  column_list = ["email", "admin"] #Não mostrar a senha

  column_searchable_list = ["email"]

  column_filters = ["email", "admin"]  
  #can_edit = False
  #can_create = False
  #can_delete = False
  @action(
    "toggle_admin",
    "Toggle admin status",
    "Are you sure?"
  )
  def toggle_admin_status(self, ids):
    users = User.query.filter(User.id.in_(ids)).all()
    total = len(users)
    for user in users:
      user.admin = not user.admin
    db.session.commit()
    flash(f"{total} usuários alterados com sucesso!", "success")

  @action(
    "send_email",
    "Send email to all users",
    "Are you sure?"
  )
  def send_email(self, ids):
    users = User.query.filter(User.id.in_(ids)).all()
    #1 redirect para um form de enviar e-mail
    #2 enviar o email
    flash(f"{len(users)} e-mails enviados", "success")

