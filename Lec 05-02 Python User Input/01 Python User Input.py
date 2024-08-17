# input() is a function whicl allows for user input

# Let us use some int value as input
num1 = 23
num2 = 32

def num_function():
    print(num1+num2)

num_function()

# input() always returns a string.
# so, we are not getting an addition
num3 = input("Number 3: ")
num4 = input("Number 4: ")

def addition():
    print(num3+num4)

addition()

# If we want a numeric type, then you need to convert the string to the appropriate type with the built-in int(), float(), or complex() function
# We have to use Type casting like below
num5 = int(input("Number 5: "))
num6 = int(input("Number 6: "))

def sum():
    print(num5+num6)

sum()

empName = input("Name: ")
empId = input("Id: ")
empSalary = float(input("Salary: "))
fullTimeEmployee = input("Full Time? ")

print("--------------------------------------")
def empInfo(empName, empId, empSalary, fullTimeEmployee):
    x = f"Employee Name: {empName.upper()} \nEmployee Id: {empId} \nEmployee Salary: {empSalary:,.2f} \nFull Time Employee: {fullTimeEmployee}"
    print(x)

# We define the variables when the function is called
empInfo(empName, empId, empSalary, fullTimeEmployee)
# empInfo(empName, empId, empSalary, fullTimeEmployee)
# User input can only accept one sets of data



