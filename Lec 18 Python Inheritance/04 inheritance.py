# Parent class
class Employee:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def printTheName(self):
        print(self.name, self.age)

# Child class Mount Sinai 
# super() function that will make the child class inherit all the methods and properties from its parent CLASS
class MountSinai(Employee):
    def __init__(self, name, age):
        super().__init__(name, age)

# using the child class Mount Siani to create an object, 
a = MountSinai("Jenifer", 43)
a.printTheName()
