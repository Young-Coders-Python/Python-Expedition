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

# Python logical operator ----> 'and', 'or', 'not'

# Built in Math function

# The max() functions can be used to find the highest value in an iterable
print(max(25436, 6354, 7286, 587264, 258762))

# The min() functions can be used to find the lowest value in an iterable
print(min(25436, 6354, 7286, 587264, 258762))

# The abs() function returns the absolute (positive) value of the specified number
print(abs(-34.567364))

# The pow(x, y) function returns the value of x to the power of y (xy).
print(a**b)
print(pow(2, 3))

print(round(3.2))
print(round(3.4))
print(round(3.5))
print(round(3.8))

# we are importing math library by below line
import math

# The math.sqrt() method returns the square root of a number
print(math.sqrt(64))

# Rounds a square root number downwards to the nearest integer
print(math.isqrt(37))

# Rounds a number down to the nearest integer
print(math.floor(3.7))

# Rounds a number up to the nearest integer
print(math.ceil(3.1))

print(math.factorial(5))

# below one gave us remainder or modulus
print(x%y)

# method returns the remainder of x with respect to y
print(math.remainder(9, 2))
print(math.remainder(9, 3))
print(math.remainder(9, 4)) # why not working with 9, 5

# we are importing date and time library
import datetime
print(datetime.datetime.now())