# The __init__() Function
'''
The examples we learned are in their simplest form, and are not really useful in real life applications.

All classes have a function called __init__(), which is always executed when the class is being initiated.

Use the __init__() function to assign values to object properties, or other operations that are necessary to do when the object is being created:
'''
class Employee:
    def __init__(self, name, age):
        self.name = name
        self.age = age

# here a1 is the object
# The __init__() function is called automatically every time the class is being used to create a new object.
a = Employee("Cahrlie", 33)
# print(a1)
print(a.name)
print(a.age)
print(f"Name: {a.name}, Age: {a.age}")

