import click

from core.main import main


@click.group()
@click.option(
    "--debug/--no-debug",
    default=False,
    help="Enable debug mode",
    envvar="DEBUG",
)
@click.pass_context
def cli(ctx: click.Context, debug: bool) -> None:
    """Tool Spotify CLI"""
    ctx.ensure_object(dict)
    ctx.obj["DEBUG"] = debug


@cli.command()
@click.option(
    "--host",
    default="localhost",
    help="Host to run the server on",
    envvar="HOST",
)
@click.option(
    "--port",
    default=8000,
    help="Port to run the server on",
    type=int,
    envvar="PORT",
)
@click.pass_context
def dev(ctx: click.Context, host: str, port: int) -> None:
    """Run the development server"""
    click.echo(f"Running development server on {host}:{port}...")
    click.echo(f"Debug mode: {ctx.obj['DEBUG']}")
    main()


@cli.command()
@click.argument("name", required=False)
@click.option("--count", default=1, help="Number of times to run")
@click.pass_context
def other(ctx: click.Context, name: str | None, count: int) -> None:
    """Run other command with optional name and count"""
    for _ in range(count):
        msg = f"Hello {name}!" if name else "Running other command..."
        click.echo(msg)
        if ctx.obj["DEBUG"]:
            click.echo("Debug mode is enabled")


def run() -> None:
    """Entry point for the CLI"""
    cli(obj={})
