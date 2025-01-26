'''
Objects can also contain methods. Methods in objects are functions that belong to the object. We created methods inside the Employee class
'''
class Employee:
    def __init__(self, name, gender, age):
        self.name = name
        self.gender = gender
        self.age = age

    # Methods -- when function present inside class
    def empName(self):
        print("Employee Name: " + self.name)

    def empGender(self):
        print("Employee Gender: " + self.gender)

    def empAge(self):
            print(f"Employee Age: {self.age}")
            # Why we use formatted text in above line?
            # because string+int is not possible like line 16

a = Employee("Douglas", "M", 71)
# what object can do? It can access class content
a.empName()
a.empGender()
a.empAge()

