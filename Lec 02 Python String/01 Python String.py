# 07/27/2024
print("Hello World!")
print('Hi')

name = "Mohammad"
print(name)
print(type(name))
# To get the length of a string, we use the len() function.
print(len(name))

# String Concatenation: when combine 2 String
# To concatenate, or combine, two strings - we can use the + operator.
print("Hello!" + "Welcome to Python") # No white space created

# We can use coma to concatenate
print("Good", "Evening")

firstName = "Mohammad"
lastName = "Sharkar"

print(firstName + lastName) 
print(firstName + " " + lastName) # This is not smart code
print(firstName, lastName) # we will use this

# We can assign a multiline string to a variable by using three double or single quotes:
a ="""My Name is Alex, 
    I am 200 years old,
    I live in NY,
    I love Python"""

print(a)
print(len(a))




print("--------------------------------------")
# Tofael's Book
# Quotes Inside Quotes
# We can use quotes inside a string, unless they don't match the quotes surrounding the string
print("Tofael's Book")
print('My Name is "Sharkar" and I am 100 years old')

print("--------------------------------------")
# for above line, there is a solution
# Escape Character for double quotation \"
print("My Name is \"Shankar\" and I am 200 years old")

print("--------------------------------------")
# Escape Character for new line, we use \n
print("My Name is \"Shankar\" and \nI am 200 years old")

print("--------------------------------------")
# Escape Character for tab, we use \t
print("\tMy Name is \"Shankar\" and \n\tI am 200 years old")

print("--------------------------------------")
# Escape Character for single quotation \'
print("\tMy Name is \"Shankar\" and \n\tI am \'200\' years old")

print("--------------------------------------")
# Escape Character \
print("My Name is \\Shankar\\ and I am 200 years old")

# String Methods
x = "Hello World!"
print(x)
print(len(x)) # len() function

# To modify the String we have some methods
print(x.upper())
print(x) # still same x, because String is immutable [not changable]

# The lower() method returns the string in lower case
print(x.lower())

# The strip() method removes any whitespace from the beginning and/or from the end.
x = "   Hakuna Matata          "
print(x)
print(x.strip())

# The strip() method cannot removes space from the middle of a String
x = "   Olive      Garden    "
print(x)
print(x.strip())

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
 
# A quick brown fox jumps over the lazy dog

# The capitalize() method returns a string where the first character is upper case, and the rest is lower case.
txt = "pACK my BoX with five dOZEN liquor JUGS"
print(txt.capitalize())

#The title() method returns a string where the first character in every word is upper case
txt = "pACK my BoX with five dOZEN liquor JUGS"
print(txt.title())

# The istitle() method returns True if all words in a text start with a upper case letter, AND the rest of the word are lower case letters, otherwise False. Symbols and numbers are ignored.
print(txt.istitle())

a = "The Rock 1?"
print(a.istitle())