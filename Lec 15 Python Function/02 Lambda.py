# User defined function or Named function

def triplet (a):
    return a*a*a
# a named function might have multiple lines of expression
# but below lmbda have only one line of expression

print(triplet(2))


# Lambda function
# This function is defines as without name [Anonymus function]
# This is not powerful as Named function
# It might have multiple parameter, but have single expression [Single line of code]
# Below a before the : is parameter and a*a*a is called expression/syntax

# We use only one parameter
# one way
print((lambda a : a*a*a)(3))

# second way
x = (lambda b: b*b*b)(4)
print(x)

# Third way
y = lambda c: c*c*c
print(y(5))

# we will use third way from now onwards

# Now We use more than one parameter (m and n), but expression or syntax is always single line [m*m + 2*m*n + n*n]
z = lambda m,n : m*m + 2*m*n + n*n
print(z(2,3))

# Why Use Lambda Functions?
# The power of lambda is better shown when you use them as an anonymous function inside another function. Say you have a function definition that takes one argument, and that argument will be multiplied with an unknown number

def my_function(n):
    return lambda a: a*n

duplicate = my_function(2)
print(duplicate(10))

triplicate = my_function(3)
print(triplicate(10))