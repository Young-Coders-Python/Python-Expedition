# Booleans represent one of two values: True or False.

# When you compare two values, the expression is evaluated and Python returns the Boolean answer

print(3>2)
print(2>3)
print(2==3)

# When we run a condition in an if or in an elif statement, Python returns True or False
a = 33
b = 51
if a>b:
    print(a, "is greater than", b)
elif a<b:
    print(a, "is less than", b) 
elif a==b:
    print(a, "is equal to", b)
else:
    print("The system failed to execute the order")

# TODO: Research the below one
# The bool() function allows you to evaluate any value, and give you True or False in return
# Returns True when the argument x is true, False otherwise.
print(bool("Hello")) # True
print(bool("")) # False
print(bool("Hello"))
print(bool(15))
print(bool(0))
print(bool(1.5))
print(bool(0.0))