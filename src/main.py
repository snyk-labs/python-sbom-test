import typer
import json

from sbom_test_api import SbomTestApi
from compare_sbom import CompareSbom

app = typer.Typer()


@app.command()
def run(input_file: str, output_file: str):
    print(f"Running application")

    print(f"Input:  {input_file}")
    print(f"Output: {output_file}")    

    api_token = ""
    org_id = ""

    sbom_api = SbomTestApi(api_token=api_token)

    with open(input_file, 'r') as input:
        data = json.load(input)

        sbom_test_result = sbom_api.run_sbom_test(org_id, data)

        with open(output_file, 'w+') as output:
            json.dump(sbom_test_result, output)

    compare = CompareSbom()

    compare.compare(input_file, output_file)

if __name__ == "__main__":
    app()