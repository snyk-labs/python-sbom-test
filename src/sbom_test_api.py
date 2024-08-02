import requests

class SbomTestApi():
    rest_api_prefix: str = "https://api.snyk.io/rest/orgs/"
    api_token: str

    def __init__(self, api_token):
        self.api_token = api_token

    def run_sbom_test(self, org_id: str, sbom_json: str):
        sbom_test_endpoint = "sbom_tests"
        url = f"{self.rest_api_prefix}{org_id}/{sbom_test_endpoint}"

        params = {
            "version": "2023-10-24%7Ebeta"
        }

        headers = {
            'Authorization': f'token {self.api_token}',
            'Accept': 'application/vnd.api+json',
            'Content-Type': 'application/vnd.api+json'
        }

        payload = {
            "data": {
                "attributes": {
                    "format": "string",
                    "sbom": sbom_json
                },
                "type": "resource"
            }            
        }

        url = url + "?version=2023-10-24%7Ebeta"

        response = requests.post(url, headers=headers, json=payload)

        if response.status_code >= 300:
            raise Exception(f"Expected 2xx response, received {response.status_code}")
        
        response_json = response.json()

        job_id = response_json.get('data').get('id')

        return self.check_job(org_id, job_id, self.api_token)
        
    def check_job(self, org_id: str, job_id: str, api_token: str):
        url = f"{self.rest_api_prefix}{org_id}/sbom_tests/{job_id}"

        url = url + "?version=2023-10-24%7Ebeta"

        headers = {
            "Accept": "application/vnd.api+json",
            "Content-Type": "application/vnd.api+json",
            "Authorization": f"token {api_token}"
        }

        response = requests.get(url, headers=headers)
            
        if response.status_code >= 300:
            raise Exception(f"Expected 2xx response, received {response.status_code}")
        
        return response.json()
