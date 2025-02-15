#!/usr/bin/env python3

from rich.console import Console
from pathlib import Path

from gjdutils import __version__
from gjdutils.decorators import console_print_doc
from gjdutils.pypi_build import (
    check_version_exists,
    clean_build_dirs,
    build_package,
    upload_to_pypi,
)
from gjdutils.shell import fatal_error_msg

console = Console()


def main():
    console.rule("[yellow]Starting Production PyPI Deployment")

    # Check if version already exists
    if check_version_exists(__version__, pypi_env="prod"):
        fatal_error_msg(
            f"Version {__version__} already exists on PyPI.\nPlease update __VERSION__.py to a new version number first."
        )

    # Confirm with user before proceeding
    version_confirm = input(
        f"\nAre you sure you want to deploy version {__version__} to production PyPI? (y/N): "
    )
    if version_confirm.lower() != "y":
        console.print("\n[yellow]Deployment cancelled by user[/yellow]")
        return

    # Execute deployment steps
    clean_build_dirs()
    build_package()
    upload_to_pypi(pypi_env="prod")

    console.print(
        "\n[green]Deployment to Production PyPI completed! run ./scripts/check_pypiprod.py[/green]"
    )


if __name__ == "__main__":
    main()
