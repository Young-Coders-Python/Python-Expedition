# Logical operators are used to combine two or more conditional statements
# and operator Returns True if both statements are true

def outcome(val1, val2):
    if val1%2==0 and val1>val2:
        print(val1, "is an even number and", val1, "is greater than", val2)
    elif val1%2==0 and val1<val2:
        print(val1, "is an even number and", val1, "is less than", val2)
    elif val1%2==0 and val1==val2:
        print(val1, "is an even number and", val1, "is equal to", val2)
    elif val1%2==0 and val1>=val2:
        print(val1, "is an even number and", val1, "is greater than or equal to", val2)
    elif val1%2==0 and val1<=val2:
        print(val1, "is an even number and", val1, "is less than or equal to", val2)
    elif val1%2==1 and val1>val2:
        print(val1, "is an odd number and", val1, "is greater than", val2)
    elif val1%2==1 and val1<val2:
        print(val1, "is an odd number and", val1, "is less than", val2)
    elif val1%2==1 and val1==val2:
        print(val1, "is an odd number and", val1, "is equal to", val2)
    elif val1%2==1 and val1>=val2:
        print(val1, "is an odd number and", val1, "is greater than or equal to", val2)
    elif val1%2==1 and val1<=val2:
        print(val1, "is an odd number and", val1, "is less than or equal to", val2)
    else:
        print("Please provide a valid number for val1 and val2")

outcome(23, 21)
outcome(35473, 764587)
outcome(20, 20)


