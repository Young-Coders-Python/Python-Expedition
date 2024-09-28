# The continue statement is used to skip the remaining code inside a loop for the current iteration only.
j = 1
while j<10:
    j+=2
    if j == 5:
        continue
    print(j)
print("Porgram End")