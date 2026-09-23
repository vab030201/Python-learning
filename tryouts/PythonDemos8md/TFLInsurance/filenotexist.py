
import json

try:

    with open("policies.json", "r") as file:
        policies = json.load(file)

except FileNotFoundError:

    print("Policy file does not exist.")
    policies = []