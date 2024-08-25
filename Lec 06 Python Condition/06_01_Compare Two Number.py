
# if is the first condition
# else is the last condition
# elif is the condition between them
# else don't need any condition
# if a condition is true, then interpreter will execute the statement inside that condition

a = 70
b = 60

if a>b:
    print(a, "is greater than", b)
elif a<b:
    print(a, "is smaller than", b)
elif a==b:
    print(a, "is equal to", b)
else:
    print("The system failed to execute this order")