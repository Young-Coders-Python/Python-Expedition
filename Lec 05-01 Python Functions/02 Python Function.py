print("--------------------------------------")
# A parameter is the variable listed inside the parentheses in the function definition.
def empInfo(empName, empId, empSalary, fullTimeEmployee):
    x = f"Employee Name: {empName.upper()} \nEmployee Id: {empId} \nEmployee Salary: {empSalary:,.4f} \nFull Time Employee: {fullTimeEmployee}"
    print(x)

# We define the variables when the function is called
# An argument is the value that is sent to the function when it is called.
# the order of the arguments does matter.
empInfo("Aymaan", 21767, 4237547235, True)
print("--------------------------------------")
# By default, a function must be called with the correct number of arguments. Meaning that if your function expects 4 arguments, you have to call the function with 4 arguments, not more, and not less.
empInfo("Nadia", 635254, 834827638, False)
print("--------------------------------------")
# We can also send arguments with the key = value syntax. This way the order of the arguments does not matter.
empInfo(empSalary = 87326472638, fullTimeEmployee = True, empName = "Alex", empId = 85276)

# Default Parameter Value. The following example shows how to use a default parameter value. If we call the function without argument, it uses the default value:

print("--------------------------------------")
def emp_info(empName, empId, empSalary = 934827638, fullTimeEmployee = True):
    x = f"Employee Name: {empName.upper()} \nEmployee Id: {empId} \nEmployee Salary: {empSalary:,.4f} \nFull Time Employee: {fullTimeEmployee}"
    print(x)
# calling the function with a different argument
emp_info("Shahriar", 335254, 134827638, False) 

print("--------------------------------------")
# calling the function without fullTimeEmployee argument
emp_info("Ishraq", 995254) 

print("--------------------------------------")
# Return Values: To let a function return a value, use the return statement
def yearlySalary(monthlySalary):
  return 12 * monthlySalary

print(yearlySalary(5000))

print("--------------------------------------")
def yearlySalary(monthlySalary):
  x = 12 * monthlySalary
  return print(x)

yearlySalary(3000)

# The pass Statement function definitions cannot be empty, but if you for some reason have a function definition with no content, put the "pass" statement to avoid getting an error.
def myfunction():
  pass
# having an empty function definition like this, would raise an error without the pass statement

