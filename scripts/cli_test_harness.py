"""Harness to make it easy to debug CLI Apps.

Script calls the CLI app with the appropriate arguments to test the functionality of the
CLI app without having to manually congifure and a vscode launch configuration for the
CLI app. This is especially useful for testing the CLI app in a development environment
where the CLI app is being actively developed and may have breaking changes that require
frequent updates to the launch configuration.

Set breakpoints in the CLI app code and run this script in debug mode to step through the
CLI app code.
"""

import subprocess

APP_NAME = "esd"


def esd_help() -> list[str]:
    """Get the help message for the CLI app."""
    return ["--help"]


def main():
    """Main function to run the CLI test harness."""
    args = esd_help()
    print(f"Running {APP_NAME} with arguments: {args}")
    result = subprocess.run([APP_NAME, *args], text=True)


if __name__ == "__main__":
    main()
