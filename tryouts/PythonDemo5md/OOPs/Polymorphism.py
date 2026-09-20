
class LifePolicy:

    def calculate_premium(self):
        return 25000
    
    
class HealthPolicy:

    def calculate_premium(self):
        return 18000
    
    
class MotorPolicy:

    def calculate_premium(self):
        return 12000
    
policies = [
    LifePolicy(),
    HealthPolicy(),
    MotorPolicy()
]

for policy in policies:
    print(policy.calculate_premium())
    

                