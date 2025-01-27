# Parent class
class Employee:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def printTheName(self):
        print(self.name, self.age)

# Child class Mount Sinai 
# the __init__() function is added to the child class (instead of the pass keyword).
# object of child class is calling the methods of parent class, which will not work, when _init_ function is present in child class
# When you add the __init__() function, the child class will no longer inherit the parent's __init__() function. Because, the child's __init__() function overrides the inheritance of the parent's __init__() function. To keep the inheritance of the parent's __init__() function, add a call to the parent's __init__() function.

class MountSinai(Employee):
    def __init__(self, name, age):
        Employee.__init__(self, name, age)

a = MountSinai("John Jay", 43)
a.printTheName()


# for line 17:
# Now we have successfully added the __init__() function, and kept the inheritance of the parent class, and we are ready to add functionality in the __init__() function.