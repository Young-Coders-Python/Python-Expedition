'''
The self parameter is a reference to the current instance of the class, and is used to access variables that belong to the class.
It does not have to be named 'self', you can call it whatever you like, but it has to be the first parameter of any function in the class
'''
class Employee:
    def __init__(this, name, age):
        this.name = name
        this.age = age

a1 = Employee("Cahrlie", 33)
print(a1.name)
print(a1.age)
print(f"Name: {a1.name}, Age: {a1.age}")

