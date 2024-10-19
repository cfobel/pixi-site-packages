from pathlib import Path
from typing import List, Optional
from ruamel.yaml import YAML


def gather_pypi_requirements(
    lock_file: Path,
    platform: str = "linux-64",
    environments: Optional[List[str]] = None,
) -> List[str]:
    """
    Gathers a list of PyPI requirements from a pixi.lock file for a specific platform and environment.

    Parameters
    ----------
    lock_file : Path
        Path to the pixi.lock file.
    platform : str, optional
        Target platform, by default 'linux-64'.
    environments : List[str], optional
        List of environments to gather requirements from, by default ['default'].

    Returns
    -------
    List[str]
        Sorted list of PyPI requirements extracted from the pixi.lock file.
    """
    if environments is None:
        environments = ["default"]

    yaml = YAML()
    with lock_file.open("r") as f:
        pixi_lock = yaml.load(f)

    pypi_requirements = sorted(
        {
            p["pypi"]
            for environment in environments
            for p in pixi_lock["environments"][environment]["packages"][platform]
            if "pypi" in p
        },
        key=lambda x: x.rsplit("/", 1)[-1],
    )

    return pypi_requirements
