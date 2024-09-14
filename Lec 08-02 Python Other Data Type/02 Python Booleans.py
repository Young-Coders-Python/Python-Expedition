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


# The bool() function allows you to evaluate any value, and give you True or False in return
# Returns True when the argument x is true, False otherwise.

# Almost any value is evaluated to True if it has some sort of content. Any string is True, except empty strings. Any number is True, except 0. Any list, tuple, set, and dictionary are True, except empty ones.

# In fact, there are not many values that evaluate to False, except empty values, such as (), [], {}, "", the number 0, and the value None. And of course the value False evaluates to False
print(bool("Hello")) # True
print(bool("")) # False

print(bool(15))
print(bool(0))

print(bool(1.5))
print(bool(0.0))