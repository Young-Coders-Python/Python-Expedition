# function, which came from Python library 
# print() to print the outcome 
# len() to know the length of String
# type() to know the type of variable

print("Hello")
print(len("Hello"))
print(type("Hello"))

print("--------------------------------------")
# User defined function
# simple One
def myFunction():
    print("This is my first created Function")

myFunction()



# By using variables
empName = "Alex Wu"
empId = 352
empSalary = 5568346.563
fullTimeEmployee = True

def empInfo():
    print(empName)
    print(empId)
    print(empSalary)
    print(fullTimeEmployee)

empInfo()

print("--------------------------------------")
# By using formatted Text
def emp_info():
    x = f"Employee Name: {empName.upper()} \nEmployee Id: {empId} \nEmployee Salary: {empSalary:,.4f} \nFull Time Employee: {fullTimeEmployee}"
    print(x)

emp_info()