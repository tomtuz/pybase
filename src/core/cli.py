import click

from core.main import main


@click.group()
def cli() -> None:
    """Tool Spotify CLI"""
    pass


@cli.command()
def dev() -> None:
    """Run the development server"""
    click.echo("Running development server...")
    main()


@cli.command()
def other() -> None:
    """Run other command"""
    click.echo("Running other...")
    # Add your implementation here


def run() -> None:
    cli()
