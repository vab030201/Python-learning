
class InsurancePolicy:

    def __init__(self, policy_id, customer, coverage):
        self.policy_id = policy_id
        self.customer = customer
        self.coverage = coverage

    def __str__(self):
        return (
            f"Policy({self.policy_id}, "
            f"Customer: {self.customer}, "
            f"Coverage: ₹{self.coverage})"
        )

    def __add__(self, other):
        if isinstance(other, InsurancePolicy):
            combined_coverage = self.coverage + other.coverage
            return InsurancePolicy("COMBINED", self.customer, combined_coverage)
        return NotImplemented

    def __lt__(self, other):
        if isinstance(other, InsurancePolicy):
            return self.coverage < other.coverage
        return NotImplemented

    def __gt__(self, other):
        if isinstance(other, InsurancePolicy):
            return self.coverage > other.coverage
        return NotImplemented


# ✅ Example usage
policy1 = InsurancePolicy("POL101", "Vibha", 50000)
policy2 = InsurancePolicy("POL102", "Vibha", 30000)

if policy1 > policy2:
    print("Policy 1 has higher coverage")
else:
    print("Policy 2 has higher coverage")
