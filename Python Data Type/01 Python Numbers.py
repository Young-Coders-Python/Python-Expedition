# There are three numeric types in Python: int, float, complex
# Variables of numeric types are created when you assign a value to them

# int
# Int, or integer, is a whole number, positive or negative, without decimals, of unlimited length.
x = 352745
print(x)
print(type(x))


# Float
# Float, or "floating point number" is a number, positive or negative, containing one or more decimals.
y = 3.4354
print(y)
print(type(y))

# Float can also be scientific numbers with an "e" to indicate the power of 10.
a = 35e3
b = 12E4
c = -87.7e2

print(a)
print(type(a))
print(b)
print(type(b))
print(c)
print(type(c))


# Complex , Will discuss in details later
# Complex numbers are written with a "j" as the imaginary part:
d = 3+5j
e = 5j
f = -5j
print(d)
print(type(d))
print(e)
print(type(e))
print(f)
print(type(f))

# Random Number
# Python does not have a random() function to make a random number, but Python has a built-in module called random that can be used to make random numbers

import random
print(random.random()) # give a float type outcome
print(random.randrange(1, 10))
# Import the random module, and display a random number between 1 to 9. 10 is excluded





