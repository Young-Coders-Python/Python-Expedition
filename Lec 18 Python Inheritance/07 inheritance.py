# Parent class
class Employee:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def printTheName(self):
        print(self.name, self.age)

# Child class Mount Sinai 
# We Add a method called welcome to the child class
class MountSinai(Employee):
    def __init__(self, name, age, gender):
        super().__init__(name, age)
        self.gender = gender

    def welcome(self):
        print("Welcome", self.name, ", Age: ", self.age, ", Gender: ", self.gender)

a = MountSinai("Elena", 34, "Female")
a.welcome()

# If we add a method in the child class [_init_()] with the same name as a function in the parent class, the inheritance of the parent method will be overridden.
