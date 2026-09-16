
#position arguments

def multiply(a, b):
    print(a * b)

multiply(5, 4)


#keyword arguments

def employee(name, department):
    print(name, department)

employee(department="HR", name="Ravi")


#default arguments

def greet(name="Student"):
    print("Welcome", name)

greet()
greet("Anita")