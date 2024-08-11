"""
@Author Mohammad Sharkar
Version:1.1
Date: 07/19/2024
"""

# here name is a variable, which is holding a data
print("--------------------------------------------------")
name = "Mohammad Sharkar"
age = 120
grade = 2.8876
usCitizen = True
# Above 4 data is not same
print(name)
print(age)
print(grade)
print(usCitizen)

print("--------------------------------------------------")
print(type(name)) # str represent string/Text type, represent by double quotation
print(type(age)) # int represent integer/numeric type, represent by no quotation
print(type(grade)) # float represent float/numeric type, represent by no quotation
print(type(usCitizen)) # bool represent boolean type [True/False], represent by no quotation

print("--------------------------------------------------")
# naming convention of variable
# we have to assign a value for a variable
x = 483
y = 488
_ = True

print(x)
print(y)
print(_)

print("--------------------------------------------------")
# Variables are case sensitive, myNAME and MYname is not same
myNAME = "Alex"
MYname = "Joe"
print(myNAME)
print(MYname)

# alpha-numeric characters means alphabet and number both allowed
# A variable name cannot start with a number
my1var = "Michael"

# How to write Multi Words Variable Names
# CamelCase, Snake case and pascal case
# Example of camel case -- myName
# Genrally variable name start with lower case, but this is not a rule, but we will follow this
myName = "Michele"
myAge = 234
myGradeScore = 3.01

# Example of pascal case -- MyName
MyName = "Michele"
MyAge = 234
MyGradeScore = 3.01

# Example of snake case -- my_name
my_name = "Boris"
my_age = 77
my_grade_score = 3.886

# Camelcase and snakecase is most popular and used in the industry, we will follow

print("--------------------------------------------------")
# Variables can even change type after they have been set.
x = 7 # int type
x = 3.0563 # float type
print(x)
print(type(x))

y = 510 # int type
y = "Bill" # str type
print(y)
print(type(y))
# because interpreter covert source code to binary code line by line, 
# last statement will be executed

print("--------------------------------------------------")
# What is casting
x = 4
print(x)
print(type(x))

y = str(4) # we cast int type to a str type
print(type(y))

z = bool("Tofael")
print(type(z))

# although the data type is different but casting allows us to get a new data type
# windows user: shift + alt + down/up arrow to copy a line
# Mac user: shift + opt + down/up arrow to copy a line
# windows user: shift + control + k to delete a line
# Mac user: shift + command + k to delete a line






