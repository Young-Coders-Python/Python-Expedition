
'''
The __str__() function controls what should be returned when the class object is represented as a string.
'''
class Employee:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}"

a1 = Employee("John", 53)
print(a1)


