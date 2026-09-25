
from operatoroverlodaing import InsurancePolicy


def __eq__(self, other):

    if isinstance(other, InsurancePolicy):
        return self.policy_id == other.policy_id

    return NotImplemented


policy1 = InsurancePolicy(
    "POL1001",
    "Ravi",
    1000000
)

policy2 = InsurancePolicy(
    "POL1002",
    "Ravi",
    500000
)

print(policy1 == policy2)