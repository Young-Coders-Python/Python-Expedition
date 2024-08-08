# String Methods
x = "A quick brown FOX jumps over the lazy DOG"
# To modify the String we have some methods

print("--------------------------------------")
print(x.upper())
print(x) # still same x, because String is immutable [not changable]

# The lower() method returns the string in lower case
print(x.lower())

print("--------------------------------------")
# The isupper() method returns True if all the characters are in upper case, otherwise False. Numbers, symbols and spaces are not checked, only alphabet characters.
print(x.isupper())

# The islower() method returns True if all the characters are in lower case, otherwise False. Numbers, symbols and spaces are not checked, only alphabet characters.
print(x.islower())

print("--------------------------------------")
# The swapcase() method returns a string where all the upper case letters to lower case and lower case letters to upper case.
print(x.swapcase());

print("--------------------------------------")
# The capitalize() method returns a string where the first character is upper case, and the rest is lower case.
txt = "pACK my BoX with five dOZEN liquor JUGS"
print(txt.capitalize())

print("--------------------------------------")
#The title() method returns a string where the first character in every word is upper case
txt = "pACK my BoX with five dOZEN liquor JUGS"
print(txt.title())

print("--------------------------------------")
# The istitle() method returns True if all words in a text start with a upper case letter, AND the rest of the word are lower case letters, otherwise False. Symbols and numbers are ignored.
print(txt.istitle())

a = "The Rock 1?"
print(a.istitle())

print("--------------------------------------")
# The isalnum() method returns True if all the characters are alphanumeric, meaning alphabet letter (a-z) and numbers (0-9).
x = "A quick brown FOX jumps over A lazy DOG"
print(x.isalnum()) # Why False? space between words

fruit = "Apple483"
print(fruit.isalnum())

print("--------------------------------------")
# The isalpha() method returns True if all the characters are alphabet letters (a-z). 
fruit = "483Apple"
print(fruit.isalpha()) # numeric number present

fruit = "Apple"
print(fruit.isalpha()) # True

print("--------------------------------------")
# The isnumeric() method returns True if all the characters are numeric (0-9), otherwise False. 
fruit = "Apple"
print(fruit.isnumeric())

fruit = "483Apple"
print(fruit.isnumeric())

fruit = "483"
print(fruit.isnumeric())

print("--------------------------------------")
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

print("--------------------------------------")
#The endswith() method returns True if the string ends with the specified value, otherwise False.
print(x.endswith("DOG")) # True
print(x.endswith("G")) # True
print(x.endswith("G", 2, 39)) # True
print(x.endswith("G", 2, 30)) # False

print("--------------------------------------")
# The strip() method removes any whitespace from the beginning and/or from the end.
x = "   Hakuna Matata          "
print(x)
print(x.strip())

# The strip() method cannot removes space from the middle of a String
x = "   Olive      Garden    "
print(x)
print(x.strip())

print("--------------------------------------")
# We can specify which character(s) to remove, if not, any whitespaces will be removed. Example of Remove the leading and trailing characters:
txt = ",,,,,rrttgg.....banana....rrr"
x = txt.strip(",.grt")
print(x) # banana

print("--------------------------------------")
# The lstrip() method removes any leading characters (space is the default leading character to remove)
# Example of Remove spaces to the left of the string:
txt = " 	banana 	"
x = txt.lstrip()
print(x)
print("of all fruits", x, "is my favorite") # of all fruits banana     is my favorite

print("--------------------------------------")
# Example of Remove the leading characters:
txt = ",,,,,ssaaww.....banana"
x = txt.lstrip(",.asw")
print(x)

print("--------------------------------------")
# The rstrip() method removes any trailing characters (characters at the end a string), space is the default trailing character to remove.
# Example of Remove any white spaces at the end of the string:
txt = " 	banana 	"
x = txt.rstrip()
print(x)
print("of all fruits", x, "is my favorite") # of all fruits     banana is my favorite

print("--------------------------------------")
# Example of Remove the trailing characters if they are commas, periods, s, q, or w:
txt = "banana,,,,,ssqqqww....."
x = txt.rstrip(",.qsw")
print(x)

print("--------------------------------------")
# The replace() method replaces a string with another string [single character, partial word, full STring]
x = "   Olive      Garden   "
print(x.replace("G", "K"))
print(x.replace("Garden", "Color"))
print(x.replace("      Garden", " Garden")) # if there is a space in the middle, we can use replace()
print(x.replace("      ", " "))

# below we used strip() and replace() together
print(x.strip().replace("      G", " G"))

a = "Good Morning"
print(a.replace("Good Morning", "Good Evening"))

# String Methods
fruit = "Banana" 
# The center() method will center align the string, using a specified character (space is default) as the fill character.
print(fruit.center(14))
print(fruit.center(14, "o"))
print(fruit.center(15, "o"))

print("--------------------------------------")
# The ljust() method will left align the string, using a specified character (space is default) as the fill character.
print(fruit.ljust(14, "o"))

print("--------------------------------------")
# The rjust() method will right align the string, using a specified character (space is default) as the fill character.
print(fruit.rjust(14, "o"))

print("--------------------------------------")
# The count() method returns the number of times a specified value appears in the string
text = "I love apples, apple are my favorite fruit"
print(text.count("a"))
print(text.count("apple"))

print("--------------------------------------")
# The find() method finds the first occurrence of the specified value.
# indexing start from 0
txt = "Pack My Box With Five Dozen Liquor Jugs"
print(txt.find("a"))
print(txt.find("o"))
print(txt.find("S"))
print(txt.find("Box"))
print(txt.find("Box", 10, 30))
print(txt.find("a", 10, 39))

print("--------------------------------------")
# The index() method finds the first occurrence of the specified value.
# The index() method is almost the same as the find() method, the only difference is that the find() method returns -1 if the value is not found. (See example below). The index() method raises an exception if the value is not found.
# print(txt.index("a", 10, 39))
print(txt.find("o"))





