print("--------------------------------------")
def empInfo(empName, empId, empSalary, fullTimeEmployee):
    x = f"Employee Name: {empName.upper()} \nEmployee Id: {empId} \nEmployee Salary: {empSalary:,.4f} \nFull Time Employee: {fullTimeEmployee}"
    print(x)

# We define the variables when the function is called
empInfo("Aymaan", 21767, 4237547235, True)
print("--------------------------------------")
empInfo("Nadia", 635254, 834827638, False)
print("--------------------------------------")
empInfo("Alex", 85276, 87326472638, True)