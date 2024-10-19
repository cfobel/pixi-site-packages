from pathlib import Path
from typing import Optional

import typer

from pixi_site_packages.core import gather_pypi_requirements

app = typer.Typer()


@app.command()
def main(
    lock_file: Path = typer.Argument(..., help="Path to the pixi.lock file."),
    output_path: Optional[Path] = typer.Option(
        None, help="Path to output the requirements.txt file. Defaults to stdout."
    ),
    platform: str = typer.Option("linux-64", help="Target platform."),
    environments: Optional[str] = typer.Option(
        None, help="Comma-separated list of environments to include."
    ),
):
    """
    Extract PyPI requirements from a pixi.lock file and optionally write them to an output file.

    Parameters
    ----------
    lock_file : Path
        Path to the pixi.lock file.
    output_path : Optional[Path]
        Path to the output file. If not specified, requirements are printed to stdout.
    platform : str
        Target platform (default: 'linux-64').
    environments : Optional[str]
        Comma-separated list of environments to include (default: 'default').
    """
    env_list = environments.split(",") if environments else ["default"]
    pypi_requirements = gather_pypi_requirements(lock_file, platform, env_list)

    if output_path:
        with output_path.open("w") as f:
            f.write("\n".join(pypi_requirements))
        typer.echo(f"requirements written to {output_path}")
    else:
        typer.echo("\n".join(pypi_requirements))


if __name__ == "__main__":
    app()
