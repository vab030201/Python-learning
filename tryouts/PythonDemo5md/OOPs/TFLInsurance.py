
class Policy:

    def __init__(
        self,
        policy_number,
        customer_name,
        policy_type,
        premium
    ):
        self.policy_number = policy_number
        self.customer_name = customer_name
        self.policy_type = policy_type
        self.premium = premium

    def display(self):
        print(self.policy_number)
        print(self.customer_name)
        print(self.policy_type)
        print(self.premium)
        
        
policy1 = Policy( "POL1001", "Rahul", "Life",25000)


policy2 = Policy( "POL1002", "Anjali", "Health",15000)        