# a single String
language = "Python"
print(language)
print(type(language))

# Python use 4 built-in data types to store collections of data: List, Tuple, Set, and Dictionary
# Lists are used to store multiple items in a single variable.
# a list of String, created using square brackets
# The name of this list is programmingLanguage
programmingLanguage = ["Python", "Java", "C++", "C#", "Javacsript", "SQL", "C++"]
print(programmingLanguage)
print(type(programmingLanguage))
# lists are defined as objects with the data type 'list'

# List items are ordered, changeable [add, remove], and allow duplicate values.
# List items are indexed and accessed by referring to the index number. the first item has index [0], the second item has index [1] etc.
print(programmingLanguage[0])
print(programmingLanguage[3])

# Negative indexing means start from the end. -1 refers to the last index, -2 refers to the second last index and so on.
print(programmingLanguage[-1])
print(programmingLanguage[-2])

# Below line print from index 0 to last index
print(programmingLanguage)

# Range of Indexes
# You can specify a range of indexes by specifying where to start and where to end the range.
# When specifying a range, the return value will be a new list with the specified items.
# Start value 1
# By leaving out the End value, the range will go on to the end of the list
print(programmingLanguage[1:])

# Start value 2 [included], End value excluded [5-1= till 4]
print(programmingLanguage[2:5])

# By leaving out the start value, the range will start at the first item
print(programmingLanguage[:5])

# Start value 1, End value excluded [5-1= till 4], increment by 2
print(programmingLanguage[1:5:2])

# returns the items from "C#" (-4) to, but NOT including "C++" (-1):
print(programmingLanguage[-4:-1])

# "in" keyword give us boolean value
print("Java" in programmingLanguage)
print("java" in programmingLanguage) # Case sensitive

# "not in" keyword also give us boolean value
print("lava" not in programmingLanguage) # Case sensitive
print("Java" not in programmingLanguage) # Case sensitive

# or we can use like below
if "Java" in programmingLanguage:
    print("Java is present in the List")
else:
    print("Java is not present in the List")

programmingLanguage = ["Python", "Java", "C++", "C#", "Javacsript", "SQL", "C++"]
print(programmingLanguage)
print(len(programmingLanguage))

# To change the value of a specific index, we ahve to refer the index number
programmingLanguage[1] = "Dart"
print(programmingLanguage)
print(len(programmingLanguage))

# If you insert more items than you replace, the new items will be inserted where you specified, and the remaining items will move accordingly
# The length of the list will change when the number of items inserted does not match the number of items replaced.
programmingLanguage[2:3] = ["Scala", "Typescript"]
print(programmingLanguage)
print(len(programmingLanguage))

programmingLanguage[2:4] = ["HTML", "Ruby", "Pearl"]
print(programmingLanguage)
print(len(programmingLanguage))

# If less values inserted than the replace, the new values will be inserted where specified, and the remaining values will be moved accordingly
programmingLanguage[2:7] = ["Kotlin"]
print(programmingLanguage)
print(len(programmingLanguage))

# Add List Items by append(), insert(), extend()

# The append() method is used to add an item to the end of the list
programmingLanguage.append("Groovy")
print(programmingLanguage)

# The insert() method inserts a value at the specified index without replacing any of the existing values
programmingLanguage.insert(1, "Julia")
print(programmingLanguage)
print(len(programmingLanguage))

# The extend() method append elements from another list to the current list end
p1 = ["C+", "Ruby"]
programmingLanguage.extend(p1)
print(programmingLanguage)

# Remove List Items

# The remove() method removes [the first occurrence] the specified value from the list
programmingLanguage.remove("C++")
print(programmingLanguage)

'''
programmingLanguage.remove("Napa")
print(programmingLanguage)
'''
# Raises ValueError if the value is not present. Used Python comments as "Napa" absent" in the list

# The pop() method can removes the specified index if mentioned.
programmingLanguage.pop(4)

# If the index is not speciifed , the pop() method removes the last item.
programmingLanguage.pop()
programmingLanguage.pop()
print(programmingLanguage)

# The del keyword can removes the specified index if mentioned
del programmingLanguage [2]
print(programmingLanguage)

# The del keyword can also delete the list completely
del programmingLanguage
# print(programmingLanguage)
# this will cause an error because "programmingLanguage" have succsesfully deleted

# The clear() method empties the list. The list still remains, but it has no content.
pl = ["Python", "Java", "C++", "C#", "Javacsript", "SQL", "C++"]
print(pl)
pl.clear()
print(pl)

# List objects have a sort() method that will sort the list alphanumerically, ascending, by default
programmingLanguage = ["Python", "Java", "C++", "C#", "Javacsript", "SQL", "Java"]
programmingLanguage.sort()
print(programmingLanguage)

# By default the sort() method is case sensitive, resulting in all capital letters being sorted before lower case letters
programmingLanguage = ["python", "Java", "C++", "C#", "javacsript", "SQL", "java"]
programmingLanguage.sort()
print(programmingLanguage)

# to get a case-insensitive sort function, use str.lower as a key function when sorting a list.
programmingLanguage.sort(key=str.lower)
print(programmingLanguage)

# The reverse() method reverses the current sorting order of the elements.
programmingLanguage = ["python", "Java", "C++", "C#", "javacsript", "SQL", "java"]
programmingLanguage.reverse()
print(programmingLanguage)

mixedNumbers = [34, 12, True, 66, 1, 7778, 2.8876, 0, 21, 443]
mixedNumbers.sort()
print(mixedNumbers)

# To sort descending, use the keyword argument reverse = True
numbers = [34, 12, 66, 1, 7778, 0, 21, 443]
numbers.sort(reverse = True)
print(numbers)

# To sort ascending, use the keyword argument reverse = False
numbers.sort(reverse = False)
print(numbers)

# The built-in List method copy() is used to copy a list.
programmingLanguage = ["Python", "Java", "C++", "C#", "Javacsript", "SQL", "Java"]
pl = programmingLanguage.copy()
print(pl) # pl is the new list copied from programmingLanguage list

# The built-in List method list() is used to copy a list too
programmingLanguage = ["Java", "C++", "C#", "Javacsript", "SQL", "Java"]
pla = list(programmingLanguage)
print(pla) 

# The : (slice) operator is used to copy a list too
programmingLanguage = ["SQL", "Java", "C++", "C#", "Javacsript", "Java"]
plan = programmingLanguage[:]
print(plan) 

# Join Two Lists by using the + operator
pl1 = ["Python", "Java", "C++", "C#", "Javacsript", "SQL"]
pl2 = ["Ruby", "Pearl", "Julia", "PHP"]
programmingLanguage = pl1 + pl2
print(programmingLanguage)

# The extend() method append elements from another list to the current list end
pl2.extend(pl1)
print(pl2)

# Returns the index of the first element with the specified value
print(programmingLanguage.index("Java"))
print(programmingLanguage.index("C#"))

# Returns the number of elements with the specified value
print(programmingLanguage.count("Java"))
print(programmingLanguage.count("Python"))



