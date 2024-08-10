fname = "Mohammad"
lname = "Sharkar"
age = 100

print(fname + lname)
# print(fname + age) # can only concatenate str to str, (not str to "int") 
print(fname, age) # this is Ok

# cannot concatenate str to "int", see below line
# print("My name: " + fname + " " + lname + ", Age" + age)

# Python Format String
fname = "Mohammad"
lname = "Sharkar"
age = 100
salary = 125000

# by formatting text, we can get a outcome of String and other data type
# this {} is called placeholder
outcome = f"My Name is {fname.upper()} {lname.upper()}, my age {age} and my salary {salary:,.2f}"
print(outcome)

cost1 = 4
print(f"Fuel price {cost1:.2f}$")

cost2 = 5
total1 = f"Gas price {cost2:.3f}$"
print(total1)

cost3 = 6
total2 = f"Gas price {cost1*cost2+cost3}$"
print(total2)

# {} is called placeholder, which hold the variable
# we can call string methods inside it
# We can do arithmetic function inside placeholder. example: price + (price*tax)
# We can Display the price with 2 or 3 decimals
# We can use a comma as a thousand separator
product = "goLD"
price = 453765
tax = 0.10

x = f'The price of "{product.title()}" is {price + (price*tax):,.3f}'
print(x)

# If we wanna use " " around a name, can we use it inside formatting text? How?
x = f"The price of \"{product.title()}\" is {price + (price*tax):,.3f}"
print(x)



