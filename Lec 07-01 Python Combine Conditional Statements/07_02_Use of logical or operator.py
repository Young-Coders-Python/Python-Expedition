# Logical operators are used to combine two or more conditional statements
# or operator returns True if one of the statements is true
# Generally we don't use logica or operator

def outcome(val1, val2):
    if val1%2==0 or val1>val2:
        print(val1, "is an even number or", val1, "is greater than", val2)

outcome(11, 9)