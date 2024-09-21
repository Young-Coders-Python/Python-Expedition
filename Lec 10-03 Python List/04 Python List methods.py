programmingLanguage = ["Python", "Java", "C++", "C#", "Javacsript", "SQL"]
print(programmingLanguage)
print(type(programmingLanguage))

# Adding new memeber teporarily
print(programmingLanguage + ["PHP"])

# List contain mixed data type
print(programmingLanguage + ["Scala", 483, 'M', 'F'])

# List is Mutable
print(programmingLanguage)

#len function
print(len(programmingLanguage))

# append function: add (something) as an attachment or supplement at the end
programmingLanguage = ["Python", "Java", "C++", "C#", "Javacsript", "SQL", "Java"]
programmingLanguage.append("PHP")
print(programmingLanguage)

# insert function: insert in a specific position
programmingLanguage.insert(1, "Scala")
print(programmingLanguage)

#remove: Remove first occurrence of value.
# Raises ValueError if the value is not present.
programmingLanguage.remove("Java")
print(programmingLanguage)

'''
programmingLanguage.remove("Napa")
print(programmingLanguage)
'''
# Sort the list in ascending order and return None.
programmingLanguage.sort()
print(programmingLanguage)

numbers = [34, 12, 66, 1, 7778, 0, 21, 443]
numbers.sort()
print(numbers)

# pop function: remove the last index
programmingLanguage.pop()
programmingLanguage.pop()
print(programmingLanguage)

print(programmingLanguage)
print(programmingLanguage[3])

# index function: give us the respective index number
programmingLanguage = ["Python", "Java", "C++", "C#", "Javacsript", "SQL", "Java"]
print(programmingLanguage.index("Java"))
print(programmingLanguage.index("C#"))

print(programmingLanguage.count("Java"))
print(programmingLanguage.count("Python"))

# another List
p1 = ["C+", "Dart"]
p2 = programmingLanguage.copy()
print(p2)

