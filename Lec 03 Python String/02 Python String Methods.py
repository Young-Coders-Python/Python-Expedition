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
# The strip() method removes any whitespace from the beginning and/or from the end.
x = "   Hakuna Matata          "
print(x)
print(x.strip())

# TODO: below methods will go after endswith() of next page

# The strip() method cannot removes space from the middle of a String
x = "   Olive      Garden    "
print(x)
print(x.strip())

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

