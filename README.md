# Overview

This repository may be used as a starting point for Python applications using Poetry for dependency management and Typer for CLI implementation.

## Setup
Need to have the following environment variables set; SNYK_TOKEN and SNYK_ORG_ID

## Running
To run, install the dependencies using `poetry install`, and execute `poetry run python src/main.py`

Alternatively, use the provided *launch.json* to specify the command to run and execute in VS Code.

## Usage
Assume with have a SBOM with PURL for the components, file is name orig-sbom1.json

You would run the following;
1. Run command: poetry run python src/main.py ./orig-sbom1.json orig-sbom1-vulns.json - this will generate a new sbom with all the vulnerabilities information
2. Run command: poetry run python src/main.py ./orig-sbom1.json new-sbom1-vulns.json orig-sbom1-vulns.json - this will pull down the newest vulnes in new-sbom1-vulns.json and compare with orig-sbom1-vulns.json to give you a diff on the command line
