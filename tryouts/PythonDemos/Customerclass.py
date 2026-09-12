
class Customer:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print("Customer:", self.name)
        print("Age:", self.age)
        
        
customer1 = Customer("Sneha", 28)        


customer1.display()