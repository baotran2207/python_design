import click
from flask.cli import FlaskGroup

from baoapi.app import create_app
from baoapi.api.schemas import UserSchema

def create_baoapi(info):
    return create_app(cli=True)


@click.group(cls=FlaskGroup, create_app=create_baoapi)
def cli():
    """Main entry point"""





@cli.command("init")
def init():
    """Create a new admin user
    """
    from baoapi.extensions import db
    from baoapi.models import User

    click.echo("create user")
    user = User(username="baotran", email="tranthanhbao2207@gmail.com", password="pass123", active=True)
    db.session.add(user)
    db.session.commit()
    click.echo("created user admin")


@cli.command("create_tables")
def create_schema():
    """Create all tables
    """
    from baoapi.extensions import db
    db.create_all()
    db.session.commit()

@cli.command("create_user")
@click.option('--user', default=1, help='Number of greetings.')
@click.option('--name', prompt='Your name',
              help='The person to greet.')
def create_new():
    """create user
    """

    user_schema = UserSchema()
    
    pass

if __name__ == "__main__":
    cli()
