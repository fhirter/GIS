import json


with open("data.json") as file:
    data = json.load(file)
    print(json.dumps(data, indent=4))