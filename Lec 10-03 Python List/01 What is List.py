# a single String
language = "Python"
print(language)
print(type(language))

# a list of String
# The name of this list id programmingLanguage
programmingLanguage = ["Python", "Java", "C++", "C#", "Javacsript", "SQL"]
print(programmingLanguage)
print(type(programmingLanguage))

# Index number from th elist
print(programmingLanguage[0])
print(programmingLanguage[3])

# -1 represent last index
print(programmingLanguage[-1])

# -2 represent second last index
print(programmingLanguage[-2])

# Below line print from index 0 to last index
print(programmingLanguage)

# initialize from index 1
print(programmingLanguage[1:])

# initialize from index 1, condition excluded [5-1= index 4]
print(programmingLanguage[2:5])

# initialize from index 1, condition excluded [5-1= index 4], increment by 2
print(programmingLanguage[1:5:2])

# in operator give us boolean value
print("Java" in programmingLanguage)
print("java" in programmingLanguage) # Case sensitive


print("lava" not in programmingLanguage) # Case sensitive
print("Java" not in programmingLanguage) # Case sensitive

