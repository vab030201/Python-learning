
import json

with open("policies.json", "r") as file:
    policies = json.load(file)

new_policy = {
    "policy_number": "POL1003",
    "customer_name": "Amit",
    "premium": 18000,
    "status": "Active"
}

policies.append(new_policy)

with open("policies.json", "w") as file:
    json.dump(policies, file, indent=4)