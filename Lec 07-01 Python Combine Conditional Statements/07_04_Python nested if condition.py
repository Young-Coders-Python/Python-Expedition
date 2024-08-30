# We can have if statements inside if statements, this is called nested if statements.

def outcome(val1, val2):
    if val1%2==0:
        if val1>val2:
            print(val1, "is an even number and", val1, "is greater than", val2)
        elif val1<val2:
            print(val1, "is an even number and", val1, "is less than", val2)
        elif val1==val2:
            print(val1, "is an even number and", val1, "is equal to", val2)
        elif val1>=val2:
            print(val1, "is an even number and", val1, "is greater than or equal to", val2)
        elif val1<=val2:
            print(val1, "is an even number and", val1, "is less than or equal to", val2)
    elif not val1%2==0:
        if val1>val2:
            print(val1, "is an odd number and", val1, "is greater than", val2)
        elif val1<val2:
            print(val1, "is an odd number and", val1, "is less than", val2)
        elif val1==val2:
            print(val1, "is an odd number and", val1, "is equal to", val2)
        elif val1>=val2:
            print(val1, "is an odd number and", val1, "is greater than or equal to", val2)
        elif val1<=val2:
            print(val1, "is an odd number and", val1, "is less than or equal to", val2)
    else:
        print("Please provide a valid number")

outcome(2, 4)
outcome(3, 4)
outcome(3, 3)