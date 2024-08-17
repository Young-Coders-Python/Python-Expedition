# input() is a function whicl allows for user input
empName = input("Employee Name: ")
empId = input("Employee Id: ")
empSalary = input("Employee Salary: ")
fullTimeEmployee = input("Full Time Employee? Ans: ")

print("--------------------------------------")
def empInfo():
    print(empName)
    print(empId)
    print(empSalary)
    print(fullTimeEmployee)

# We define the variables when the function is called
empInfo()

# Let us use some int value as input
num1 = 23
num2 = 32

def num_function():
    print(num1+num2)

num_function()

# inpiut function only provide String type input
# we are not getting an addition
num3 = input("Number 3: ")
num4 = input("Number 4: ")

def addition():
    print(num3+num4)

addition()

# We have to use Type casting like below
num5 = int(input("Number 5: "))
num6 = int(input("Number 6: "))

def sum():
    print(num5+num6)

sum()
