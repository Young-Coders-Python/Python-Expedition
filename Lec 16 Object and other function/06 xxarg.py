def student (id, name):
    print(id, name)

student(101, "Alex")
student(102, "Brian")

# If you are not sure how many parameters gonna come, you can use ** before parameter 
# this is called double argument which provide dictionary type value

def stu (**detail):
    print(detail)

stu(name ="Alex", id = 101, grade = 3.768, fullTimeStudent = True)
