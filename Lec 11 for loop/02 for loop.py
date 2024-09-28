# A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).

for i in range(13):
    print(i)

print("---------------------------------")
for i in range(7, 13):
    print(i)

print("---------------------------------")
for i in range(7, 13, 2):
    print(i)

print("------------- for loop is iterating over String --------------------")
for i in "Python":
    print(i)

print("---------------------------------")
programmingLanguage = ["Python", "Java", "C++", "C#", "Javacsript", "SQL", "Java"]
for i in programmingLanguage:
    print(i)

print("-------------- Use of break -------------------")
programmingLanguage = ["Python", "Java", "C++", "C#", "Javacsript", "SQL", "Java"]
for i in programmingLanguage:
    if i == "C#":
        break
    print(i)

print("------------- Use of continue --------------------")
programmingLanguage = ["Python", "Java", "C++", "C#", "Javacsript", "SQL", "Java"]
for i in programmingLanguage:
    if i == "C#":
        continue
    print(i)

print("---------------------------------")
# The else keyword in a for loop specifies a block of code to be executed when the loop is finished
for i in range(6):
    print(i)
else:
    print("Loop ENDED")

print("---------------------------------")
# The else block will NOT be executed if the loop is stopped by a break statement.
for i in range(6):
    if i == 4:
        break
    print(i)
else:
    print("Loop ENDED")

print("-------------- nested for loop -------------------")
programmingLanguage = ["Python", "Java", "C++", "C#"]
status = ["Easy", "Hard"]
for i in programmingLanguage:
    for j in status:
        print(i, j)

print("---------------------------------")
# for loops cannot be empty, but if you for some reason have a for loop with no content, put in the pass statement to avoid getting an error.
for i in range(6):
    pass
    