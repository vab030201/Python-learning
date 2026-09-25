
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
        
policy1 = InsurancePolicy( "POL1001", "Ravi", 1000000 )

policy2 = InsurancePolicy( "POL1002", "Ravi", 500000 )        


print(policy1)
print(policy2)