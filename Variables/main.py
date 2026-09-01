
#variable 
name = "Vibha"
print (name)

#no variable declaration

#dynamic typing- no need to declare the type of variable
age = 25
print(age)
age = "twenty-five"
print(age)  

#static typing- type of variable is declared
age: int = 25
print(age)
age: str = "twenty-five"
print(age)


#dynamic binding- variable can be bound to different types of values at different times
x = 5
print(x)
x = 10
print(x)    

#static binding- variable is bound to a specific type of value at compile time
y: int = 5
print(y)

#special syntax for declaring a variable with a specific type
a = 5;b = 10;c = 15
print(a,b,c)


a,b,c = 1,3,2
print(a,b,c)