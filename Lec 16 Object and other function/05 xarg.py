def student (id, name):
    print(id, name)

student(101, "Alex")
student(102, "Brian")

# If you are not sure how many parameters gonna come, you can use * before parameter 
# this is called xargument which provide tuple type value

def stu (*detail):
    print(detail)

print(type(stu))
stu("Alex")
stu("Alex", 101)
stu("Alex", 101, 3.768, True)