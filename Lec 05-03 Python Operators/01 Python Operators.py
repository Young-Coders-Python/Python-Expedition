# Operators are used to perform operations on variables and values.
# In the example below, we use the + operator to add together two values:
print(5+7)

# Python Arithmetic operators [line 6-31]

x = 20
y = 6
# Addition
print(x + y)

# Subtraction
print(x-y)

# Multiplication
print(x*y)

# Division
print(x/y)
# The above division gave us a float number
# but if you need a solid number or int number, not a float, what you will use? see below

# Floor division [new]
print(x//y)

# Modulus or remainder
print(x%y)

# Exponentiation
a = 2
b = 5
print(a**b)

'''
The = operator is used for assignment, such as when assigning a value to a variable. The == operator is the relational operator for checking equality of two values. If the values are the same, it will return True , and will return False otherwise.
'''

print("--------------------------------------")
# Python Comparison Operators
m = 6 # here you assign a value for m
n = 4

# Equal
print(m==n) # here you compare the value

# Not Equal
print(m!=n)

# Greater than
print(m>n)

# Less than
print(m<n)

# Greater than or equal to
print(m>=n)

# Less than or equal to
print(m<=n)