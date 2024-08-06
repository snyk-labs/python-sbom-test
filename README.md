# Overview

This repository may be used as a starting point for Python applications using Poetry for using Snyk SBOM test and to get a simple diff between scans.

## Setup
Need to have the following environment variables set: SNYK_TOKEN and SNYK_ORG_ID

## Running
To run, install the dependencies using `poetry install`, and execute `poetry run python src/main.py`

Alternatively, use the provided *launch.json* to specify the command to run and execute in VS Code.

## Usage
In this example, we assume you already have a SBOM file with the components that is named orig-sbom1.json

1. Generate a new SBOM with all the vulnerabilities information:

`poetry run python src/main.py ./orig-sbom1.json orig-sbom1-vulns.json`

2. Pull down the newest vulnerabilities in a new JSON file and compare with the previous vulnerabilities JSON (from the command above). The diff is given in the terminal output:

`poetry run python src/main.py ./orig-sbom1.json new-sbom1-vulns.json orig-sbom1-vulns.json`


