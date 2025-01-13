# we wanna use a function to know who is largest by comparison
def largest(a, b):
    if a>b:
        return a
    elif a<b:
        return b
    else:
        return a==b

# the below function will not give you any outocme as no print option
largest(20, 30)

# use print function
print(largest(20, 30))

# also we can define the function with a variable
m = largest(10, 10)
print(m)

# but what is the difference between non return and return type method?
def sum (a, b):
    x = a+b
    return x

y = sum (5, 6)
print(y)

# above one we can do same without return function
# what is the advantage of return function. Ans: we can do additional action on a function

z = sum (7, 8)
z = z+1 # this kind of addditional action are done when you use return type
print(z)


