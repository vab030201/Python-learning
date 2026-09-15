
class Policy:
    
    def __init__(self, policy_number, policy_type, premium_amount):
        self.policy_number = policy_number
        self.policy_type = policy_type
        self.premium_amount = premium_amount    
        
        
    def display(self):
        print("Policy Number:", self.policy_number)
        print("Policy Type:", self.policy_type)
        print("Premium Amount:", self.premium_amount)    
        
        
policy1 = Policy(
"POL123", "Health", 5000
)
policy1.display()