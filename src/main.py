import typer

from typing_extensions import Annotated

import json
import os

from sbom_test_api import SbomTestApi
from compare_sbom import CompareSbom

app = typer.Typer()


@app.command()
def run(input_sbom: str, output_sbom: str, orig_sbom: Annotated[str, typer.Argument()] = ""):
    """
    Read input_sbom in CycloneDX format and send to Snyk SBOM Test API endpoint. 
    
    Any vulnerabilities found in the SBOM will be printed to console. 
    
    If optional paramter orig_sbom is provided, the newly generated SBOM will be compared to the original, 
    and the differences will be printed to console.
    """
    print(f"Input:  {input_sbom}")
    print(f"Orig:   {orig_sbom}")
    print(f"Output: {output_sbom}")

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

    diff = compare.diff(output_sbom, orig_sbom)

    print(diff)

if __name__ == "__main__":
    app()