import jsondiff
import json

class CompareSbom():
    def __init__(self):
        pass

    def compare(self, file_a: str, file_b: str = ""):
        input_vulns = self.load_sbom_vulns(file_a)

        if file_b == "":
            print("Identified vulns:")
            for vuln in input_vulns:
                print (f" - {vuln}")

            ret_obj = {
                "identified_vulns": input_vulns
            }

            return ret_obj
        
        else:
            output_vulns = self.load_sbom_vulns(file_b)

            fixed_vulns = []
            existing_vulns = []
            new_vulns = []

            for vuln in output_vulns:
                if vuln in input_vulns:
                    existing_vulns.append(vuln)
                else:
                    new_vulns.append(vuln)

            for vuln in input_vulns:
                if vuln not in output_vulns:
                    fixed_vulns.append(vuln)

            print("Existing vulns:")
            for vuln in existing_vulns:
                print(f" - {vuln}")

            print("")

            print("New vulns:")
            for vuln in new_vulns:
                print(f" - {vuln}")
            
            print("")

            print("Fixed vulns:")
            for vuln in fixed_vulns:
                print(f" - {vuln}")
            
            print("")

            ret_obj = {
                "existing_vulns": existing_vulns,
                "new_vulns": new_vulns,
                "fixed_vulns": fixed_vulns
            }

            return ret_obj

    def diff(self, new_sbom: str, orig_sbom: str = ""):
        new_sbom_json = self.load_sbom(new_sbom)

        if orig_sbom == "":
            return new_sbom_json

        orig_sbom_json = self.load_sbom(orig_sbom)

        return jsondiff.diff(new_sbom_json, orig_sbom_json)

    def load_sbom(self, file: str):
        with open(file, 'r') as input:
            return json.load(input)
    
    def load_sbom_vulns(self, file: str):
        with open(file, 'r') as input:
            input_json = json.load(input)

            data = input_json.get("data")
            relationships = data.get("relationships")
            vulns = relationships.get("vulnerabilities").get("data")
            
            vuln_ids = []

            for vuln in vulns:
                vuln_ids.append(vuln.get("id"))
            
            return vuln_ids


        
