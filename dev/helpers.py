import subprocess
import sys

import click


def run_command(cmd: list[str], error_msg: str) -> None:
    """Run a command and handle errors"""
    try:
        result = subprocess.run(cmd, check=True, capture_output=True, text=True)
        if result.stdout:
            click.echo(result.stdout)
        if result.stderr:
            click.echo(result.stderr, err=True)
    except subprocess.CalledProcessError as e:
        click.echo(f"Error: {error_msg}", err=True)
        if e.stdout:
            click.echo(e.stdout)
        if e.stderr:
            click.echo(e.stderr, err=True)
        sys.exit(1)
    except FileNotFoundError:
        click.echo(
            "Error: Command not found. Please ensure all dependencies are installed.",
            err=True,
        )
        sys.exit(1)


def install(dev: bool = True) -> None:
    """Install project dependencies"""
    cmd = ["poetry", "install"]
    if not dev:
        cmd.append("--no-dev")
    run_command(cmd, "Failed to install dependencies")


def test(verbose: bool = False, coverage: bool = False) -> None:
    """Run tests with optional coverage"""
    cmd = ["pytest"]
    if verbose:
        cmd.append("-v")
    if coverage:
        cmd.extend(["--cov=src", "--cov-report=term-missing"])
    run_command(cmd, "Tests failed")


def lint(path: str | None = None) -> None:
    """Run linting"""
    cmd = ["ruff", "check"]
    if path:
        cmd.append(path)
    run_command(cmd, "Linting failed")


def lintF(path: str | None = None) -> None:
    """Run linting with auto-fix"""
    cmd = ["ruff", "check", "--fix"]
    if path:
        cmd.append(path)
    run_command(cmd, "Linting with auto-fix failed")


def typecheck(path: str | None = None) -> None:
    """Run type checking"""
    cmd = ["mypy"]
    if path:
        cmd.append(path)
    else:
        cmd.append(".")
    run_command(cmd, "Type checking failed")


def format(path: str | None = None) -> None:
    """Format code and sort imports"""
    # Sort imports
    cmd = ["ruff", "check", "--select", "I", "--fix"]
    if path:
        cmd.append(path)
    run_command(cmd, "Import sorting failed")

    # Format code
    cmd = ["ruff", "format"]
    if path:
        cmd.append(path)
    run_command(cmd, "Code formatting failed")
