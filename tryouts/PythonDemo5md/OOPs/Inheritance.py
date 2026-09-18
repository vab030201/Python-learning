
class Employee:

    def __init__(self, employee_id, name):
        self.employee_id = employee_id
        self.name = name

    def display(self):
        print(self.employee_id, self.name)
        
        
class Agent(Employee):

    def sell_policy(self):
        print("Selling insurance policy")
        
class ClaimsOfficer(Employee):

    def process_claim(self):
        print("Processing claim")                