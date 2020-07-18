import click
from keysfood.ext.db import db
from keysfood.ext.auth.models import User

@click.option("--email", "-e")
@click.option("--passwd", "-p")
@click.option("--admin", "-a", is_flag=True, default=False)
def add_user(email, passwd, admin):
    """Add a new user"""
    user = User(
        email=email,
        passwd=passwd,
        admin=admin
    )
    db.session.add(user)
    db.session.commit()
    click.echo(f"Usuário {email} criado com suecesso!")

def list_users():
    users = User.query.all()
    click.echo(f"Lista de usuários {[user.email for user in users]}")