import click
from keysfood.ext.db import db
from keysfood.ext.site import models # noqa

def init_app(app):

    @app.cli.command()
    def create_db():
        """This command initializes a db"""
        db.create_all()

    @app.cli.command()
    def listar_pedidos():
        #TODO: usar tabulate
        click.echo("Lista de pedidos")
    
    @app.cli.command()
    def listar_usuarios():
        click.echo("Lista de usuários")
