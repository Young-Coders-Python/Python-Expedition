class Employee:
    def __init__(self, name, age):
        self.name = name
        self.age = age

a = Employee("Ford", 39)
print(f"Name: {a.name}, Age: {a.age}")

# We can delete the age property from the a object like below by using the del keyword
del a.age
'''
If you run it, it will shows below error
AttributeError: 'Employee' object has no attribute 'age'
'''
print(f"Name: {a.name}, Age: {a.age}")

