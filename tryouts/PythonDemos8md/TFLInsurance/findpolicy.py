
import json


def find_policy(policy_number):

    with open("policies.json", "r") as file:
        policies = json.load(file)

    for policy in policies:

        if policy["policy_number"] == policy_number:
            return policy

    return None

policy = find_policy("POL1001")

print(policy)