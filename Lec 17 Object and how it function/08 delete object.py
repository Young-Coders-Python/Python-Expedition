class Employee:
    def __init__(self, name, age):
        self.name = name
        self.age = age


a = Employee("Ford", 39)
print(f"Name: {a.name}, Age: {a.age}")

# We can delete the a object like below by using the del keyword
del a
'''
If you run it, it will shows below error
NameError: name 'a' is not defined
'''
print(f"Name: {a.name}, Age: {a.age}")

