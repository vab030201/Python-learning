
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

    # + operator
    def __add__(self, other):

        if isinstance(other, InsurancePolicy):

            combined_coverage = (
                self.coverage + other.coverage
            )

            return InsurancePolicy(
                "COMBINED",
                self.customer,
                combined_coverage
            )

        return NotImplemented

    # == operator
    def __eq__(self, other):

        if isinstance(other, InsurancePolicy):
            return self.policy_id == other.policy_id

        return NotImplemented

    # < operator
    def __lt__(self, other):

        if isinstance(other, InsurancePolicy):
            return self.coverage < other.coverage

        return NotImplemented

    # > operator
    def __gt__(self, other):

        if isinstance(other, InsurancePolicy):
            return self.coverage > other.coverage

        return NotImplemented