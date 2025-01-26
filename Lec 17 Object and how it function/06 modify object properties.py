class Employee:
    def __init__(self, name, age):
        self.name = name
        self.age = age


a = Employee("Ford", 39)
print(f"Name: {a.name}, Age: {a.age}")

# We can modify properties on objects like below
a.name = "Joe"
a.age = 38
print(f"Name: {a.name}, Age: {a.age}")

