# compareTwoNumber is an user define function
# a and b is called parameter

def compareTwonumber(a, b):
    if a>b:
        print(a, "is greater than", b)
    elif a<b:
        print(a, "is smaller than", b)
    elif a==b:
        print(a, "is equal to", b)
    else:
        print("The system failed to execute this order")

# what is the advantage of creating parametrized function?
# you can reuse the function by different arguments
# Here 2 value is called argument
compareTwonumber(2312, 2312)
compareTwonumber(312, 34)
compareTwonumber(12, 55)
