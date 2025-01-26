class student:
    # these variables are under/inside a class or member of the class
    id = ""
    name = ""

# what is an object? how we create object?
# here a is an object of the student class, it represented like below
a = student()

# the best way to know, a is an object of student class or not, we use below boolean method
print(isinstance(a, student))

# what an object can do?
# we can create object, who can access the members of a class
a.id = 203
a.name = "Alex"
print(a.id , a.name)

# by using formatted text
print(f"Name: {a.name}, Id: {a.id}")

# How many object we can create?
# b is an object of the same class
b = student()
b.name = "Brian"
b.id = 102
# by using formatted text
print(f"Name: {b.name}, Id: {b.id}")