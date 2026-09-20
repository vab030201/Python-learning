
policies = {
    "POL1001": "Life Insurance",
    "POL1002": "Health Insurance"
}

def get_policy(policy_number):

    if policy_number not in policies:
        raise KeyError(
            f"Policy {policy_number} does not exist."
        )

    return policies[policy_number]

try:

    policy = get_policy("POL9999")
    print(policy)

except KeyError as ex:

    print("Policy error:", ex)