# String Methods
fruit = "Banana" 

# The center() method will center align the string, using a specified character (space is default) as the fill character.
print(fruit.center(14))
print(fruit.center(14, "o"))
print(fruit.center(15, "o"))

# The ljust() method will left align the string, using a specified character (space is default) as the fill character.
print(fruit.ljust(14, "o"))

# The rjust() method will right align the string, using a specified character (space is default) as the fill character.
print(fruit.rjust(14, "o"))

# The count() method returns the number of times a specified value appears in the string
text = "I love apples, apple are my favorite fruit"
print(text.count("a"))
print(text.count("apple"))

# The startswith() method returns True if the string starts with the specified value, otherwise False.
x = "A quick brown FOX jumps over A lazy DOG"
print(x.startswith("A"));
print(x.startswith("B"));
print(x.startswith("A qui"));

print(len(x))
print(x.startswith("A", 0, 25)); # True
print(x.startswith("A", 1, 40)); # False
print(x.startswith("q", 2, 40)); # True
print(x.startswith("Q", 2, 40)); # False, String is case sensitive

#The endswith() method returns True if the string ends with the specified value, otherwise False.
print(x.endswith("DOG")) # True
print(x.endswith("G")) # True
print(x.endswith("G", 2, 39)) # True
print(x.endswith("G", 2, 30)) # False

# The find() method finds the first occurrence of the specified value.
# indexing start from 0
txt = "Pack My Box With Five Dozen Liquor Jugs"
print(txt.find("a"))
print(txt.find("o"))
print(txt.find("S"))
print(txt.find("Box"))
print(txt.find("Box", 10, 30))
print(txt.find("a", 10, 39))

# The index() method finds the first occurrence of the specified value.
# The index() method is almost the same as the find() method, the only difference is that the find() method returns -1 if the value is not found. (See example below). The index() method raises an exception if the value is not found.
# print(txt.index("a", 10, 39))
print(txt.find("o"))

x = "A quick brown FOX jumps over A lazy DOG"
print(x.isalnum()) # Why False? space between words

fruit = "Apple483"
print(fruit.isalnum())

fruit = "483Apple"
print(fruit.isalpha()) # numeric number present

fruit = "Apple"
print(fruit.isalpha()) # True

fruit = "Apple"
print(fruit.isnumeric())

fruit = "483Apple"
print(fruit.isnumeric())

fruit = "483"
print(fruit.isnumeric())

