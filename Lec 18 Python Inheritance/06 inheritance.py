# Parent class
class Employee:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def printTheName(self):
        print(self.name, self.age)

# Child class Mount Sinai 
# We Add a property called gender to the child class Mount Sinai
# We can get the value , line 20
class MountSinai(Employee):
    def __init__(self, name, age, gender):
        super().__init__(name, age)
        self.gender = gender

# using the child class Mount Siani to create an object, 
a = MountSinai("Jenifer", 43, "Female")
print(a.gender)
