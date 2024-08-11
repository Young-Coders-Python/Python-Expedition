# 07/27/2024
print("Hello World!")
print('Hi')

name = "Mohammad"
print(name)
print(type(name))

# To get the length of a string, we use the len() function.
print(len(name))

print("--------------------------------------")
# String Concatenation: when combine 2 String
# To concatenate, or combine, two strings - we can use the + operator.
print("Hello!" + "Welcome to Python") # No white space created --> "Hello!Welcome to Python"

# We can use coma to concatenate which provide space between String
print("Good", "Evening")

print("--------------------------------------")
firstName = "Mohammad"
lastName = "Sharkar"

print(firstName + lastName) 
print(firstName + " " + lastName) # This is not smart code
print(firstName, lastName) # we will use this

print("--------------------------------------")
# We can assign a multiline string to a variable by using three double or single quotes (not common)
a ="""My Name is Alex, 
    I am 200 years old,
    I live in NY,
    I love Python"""

print(a)
print(len(a))

print("--------------------------------------")
# Quotes Inside Quotes: Tofael's Book
# We can use quotes inside a string, unless they don't match the quotes surrounding the string
print("Tofael's Book")
print('My Name is "Sharkar" and I am 100 years old')

print("--------------------------------------")
# for above line, there is a solution
# Escape Character for double quotation \", we use around Shankar
print("My Name is \"Shankar\" and I am 200 years old")

print("--------------------------------------")
# Escape Character for new line, we use \n before I am
print("My Name is \"Shankar\" and \nI am 200 years old")

print("--------------------------------------")
# Escape Character for tab, we use \t before I am
print("\tMy Name is \"Shankar\" and \n\tI am 200 years old")

print("--------------------------------------")
# Escape Character for single quotation \' around 200
print("\tMy Name is \"Shankar\" and \n\tI am \'200\' years old")

print("--------------------------------------")
# Escape Character \
print("My Name is \\Shankar\\ and I am 200 years old")

