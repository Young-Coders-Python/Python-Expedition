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

