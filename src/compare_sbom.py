import jsondiff
import json

class CompareSbom():
    def __init__(self):
        pass

    def compare(self, file_a: str, file_b: str):
        with open(file_a, 'r') as input:
            input_json = json.load(input)

            with open(file_b, 'r') as output:
                output_json = json.load(output)

                print(jsondiff.diff(input_json, output_json))


        
