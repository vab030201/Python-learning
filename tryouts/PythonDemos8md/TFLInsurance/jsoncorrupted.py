
import json

try:

    with open("policies.json", "r") as file:
        policies = json.load(file)

except FileNotFoundError:

    print("Policy file not found.")
    policies = []

except json.JSONDecodeError:

    print("Policy file contains invalid JSON.")
    policies = []