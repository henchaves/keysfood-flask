import click
from keysfood.ext.db import db
from keysfood.ext.site import models


def init_app(app):

    @app.cli.command()
    def create_db():
        """This command initializes a db"""
        db.create_all()

    @app.cli.command()
    @click.option("--email", "-e")
    @click.option("--passwd", "-p")
    @click.option("--admin", "-a", is_flag=True, default=False)
    def add_user(email, passwd, admin):
        """Add a new user"""
        user = models.User(
            email=email,
            passwd=passwd,
            admin=admin
        )
        db.session.add(user)
        db.session.commit()
        click.echo(f"Usuário {email} criado com suecesso!")

    @app.cli.command()
    def listar_pedidos():
        #TODO: usar tabulate
        click.echo("Lista de pedidos")
    
    @app.cli.command()
    def listar_usuarios():
        click.echo("Lista de usuários")
