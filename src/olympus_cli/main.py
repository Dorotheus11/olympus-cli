"""olympus-cli entry point."""
import click
from rich.console import Console

console = Console()

@click.group()
@click.version_option()
def cli():
    """Mount Olympus CLI."""
    pass

@cli.command()
def status():
    """Show system health."""
    console.print("[bold green]Mount Olympus[/] is operational.")

@cli.command()
@click.argument("god_name")
def ping(god_name):
    """Ping a god."""
    console.print(f"Pinging [bold]{god_name}[/]...")

@cli.command()
def gods():
    """List all gods."""
    console.print("[dim]Fetching god registry...[/]")

if __name__ == "__main__":
    cli()
