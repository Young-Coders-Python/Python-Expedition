# Parent class
class Employee:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def printTheName(self):
        print(self.name, self.age)

# Child class Mount Sinai will inherit the properties and methods from the Parent class Employee
# We Use the pass keyword when you do not want to add any other properties or methods to the class
class MountSinai(Employee):
    pass

# using the child class Mount Siani to create an object, 
a = MountSinai("John Jay", 43)
# object of child class is calling the methods of parent class
a.printTheName()