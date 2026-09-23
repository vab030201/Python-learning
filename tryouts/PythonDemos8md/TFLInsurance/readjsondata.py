
import json

with open("policies.json", "r") as file:
    policies = json.load(file)
    
print(policies)   