# This is a list
# A list is a collection which is ordered and changeable.
# Lists are written with square brackets.
programmingLanguage = ["Python", "Java", "C++", "C#", "Javacsript", "SQL", "Java"]


# This is a tuple
# A tuple is a collection which is ordered and unchangeable.
# Tuples are written with parenthesis (round brackets).
fruits = ("Apple", "Orange", "Grapes", "Kiwi", "Cherry", "Fig", "Blueberry")
print(fruits)
print(type(fruits))


print(len(fruits))

# One item tuple, we should remember the comma
fruit = ("Strawberry",)
print(type(fruit))

mixedData = ("Apple", "Orange", "Grapes", 365543, False, 2.33)
print(mixedData)
print(type(mixedData))

fruits = ("Apple", "Orange", "Grapes", "Kiwi", "Cherry", "Fig", "Blueberry")
print(fruits[0])
print(fruits[1])
print(fruits[-1])

# Range of Indexes
fruits = ("Apple", "Orange", "Grapes", "Kiwi", "Cherry", "Fig", "Blueberry")
print(fruits[3:6])

# By leaving out the start value, the range will start at the first item
print(fruits[:5])

# By leaving out the end value, the range will go on to the end of the tuple
print(fruits[2:])

# Specify negative indexes if we want to start the search from the end of the tuple
print(fruits[-4:-1])


fruits = ("Apple", "Orange", "Grapes", "Kiwi", "Cherry", "Fig", "Blueberry")
print("Fig" in fruits)
print("Gig" in fruits)
print("Pig" not in fruits)

if "Orange" in fruits:
    print("Orange is present in the Tuple")
else:
    print("Orange is not present in the Tuple")


# A tuple is a collection which is ordered and unchangeable [immutable]
# How to update Tuple?
fruits = ("Apple", "Orange", "Grapes", "Kiwi", "Cherry", "Fig", "Blueberry")

# We have to convert tuple to list
fruitsAsAList = list(fruits)
print(fruitsAsAList)
print(type(fruitsAsAList))

# When a tuple turned to a list, we can use all the possible methods of list 
fruitsAsAList[2]="Raspberry"

# We have to convert list to tuple
fruitsAsATuple = tuple(fruitsAsAList)
print(fruitsAsATuple)

# Add tuple to a tuple, by + operator
fr1 = ("Apple", "Orange", "Grapes", "Kiwi")
fr2 = ("Fig",)

fruits = fr1 + fr2
print(fruits)

# When we create a tuple, we normally assign values to it. called, Packing a tuple
fr = ("Apple", "Orange", "Grapes")

#  In Python, it's allowed to extract the values back into variables. This is called "unpacking"
fr = ("Apple", "Banana", "Grapes")
(green, yellow, violet) = fr

print(green)
print(yellow)
print(violet)

print("--------------------- for loop ---------------------------")
fruits = ("Apple", "Orange", "Grapes", "Kiwi", "Cherry", "Fig", "Blueberry")
for i in fruits:
    print(i)

print("--------------------- for loop by range ---------------------------")
for i in range(len(fruits)):
    print(fruits[i])

print("--------------------- while loop ---------------------------")
i = 0
while i < len(fruits):
    print(fruits[i])
    i+=1

# Return the number of times the value 3 appears in the tuple
thisTuple = (1, 3, 3, 1, 6, 3, 8, 3, 9, 0, 4, 3)
x = thisTuple.count(3)
print(x)

# The index() method finds the first occurrence of the specified value 3
y = thisTuple.index(3)
print(y)





