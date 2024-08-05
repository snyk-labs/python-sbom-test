import typer
import json
import os

from sbom_test_api import SbomTestApi
from compare_sbom import CompareSbom

app = typer.Typer()


@app.command()
def run(input_sbom: str, output_sbom: str, orig_sbom: str = ""):
    print(f"Running application")

    print(f"Input:  {input_sbom}")
    print(f"Output: {orig_sbom}")    

    api_token = os.environ["SNYK_TOKEN"]
    org_id = os.environ["SNYK_ORG_ID"]

    sbom_api = SbomTestApi(api_token=api_token)

    with open(input_sbom, 'r') as input:
        data = json.load(input)

        sbom_test_result = sbom_api.run_sbom_test(org_id, data)

        with open(output_sbom, 'w+') as output:
            json.dump(sbom_test_result, output)

    compare = CompareSbom()

    compare.compare(output_sbom, orig_sbom)

if __name__ == "__main__":
    app()