def student (id, name):
    print(id, name)

student(101, "Alex")
student(102, "Brian")

# If you are not sure how many parameters gonna come, you can use ** before parameter 
# this is called double argument which provide dictionary type value

def stu (**detail):
    print(detail)
    # we can also ask for a specific value by calling the key like below
    print(detail["grade"])

stu(name ="Alex", id = 101, grade = 3.768, fullTimeStudent = True)

# Another example
def my_function(**kid):
    print("His last name is " + kid["lname"])

my_function(fname = "Tobias", lname = "Refsnes")