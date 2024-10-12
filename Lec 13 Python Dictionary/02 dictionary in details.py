# Dictionaries are used to store data values in key:value pairs and can be referred to by using the key name.
# A dictionary is a collection which is ordered*, changeable [change, add or remove items] and do not allow duplicates.
# As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.
# Dictionaries are written with curly brackets, and have keys and values

car = {
    "brand": "Cadillac",
    "model": "XT6",
    "year": 2023
}

print(car)
print(type(car))
print(len(car))

# Dictionary items can be accessed by referring to its key name, inside square brackets
print(car["brand"])
print(car["year"])

# get() method do the same function
print(car.get("model"))

# Dictionaries cannot have two items with the same key
# Duplicate values will overwrite existing values
car = {
    "brand": "Cadillac",
    "model": "XT6",
    "year": 2023,
    "year": 2024
}
print(car)

# The values in dictionary items can be of any data type, like int, String, float, Boolean, tuple, list etc.
car = {
    "brand": "Cadillac",
    "model": "XT6",
    "year": (2023, 2024),
    "rating": 9.80,
    "color": ["Black", "White", "Red"],
    "madeInUSA": True
}
print(car)

# We can make a dictionary by using the dict() method [not common]
info = dict(name = "Alex", age = 37, grade = 3.534, fullTimeStudent = True)
print(info)
print(type(info))

# The keys() method will return a list of all the keys in the dictionary
print(car.keys())

# The values() method will return a list of all the values in the dictionary
print(car.values())

# The items() method will return each item of a dictionary, as tuples inside a list
print(car.items())

# To determine if a specified key is present in a dictionary, the "in" keyword is used
print("rating" in car)
print("bating" in car)

if "brand" in car:
    print("brand is present as key")
else:
    print("brand is not present as key")

# A dictionary is changeable [change, add or remove items] 
# Adding an item is done by using a new index key and assigning a value to it
# driveType, transmission, engine
car = {
    "brand": "Cadillac",
    "model": "XT6",
    "year": 2024
}
print(car)
car ["color"] = "Black"
car ["bodyStyle"] = "SUV"
print(car)

# Change [Edit] a new item to the original dictionary
car = {
    "brand": "Cadillac",
    "model": "XT6",
    "year": 2024,
    "color": "Black",
    "bodyStyle": "SUV"
}
print(car)
car["model"] = "XT5"
car["color"] = "Red"
print(car)

# The update() method will update the dictionary with the items from the given argument.
# The argument must be a dictionary, or an iterable object with key:value pairs
car = {
    "brand": "Cadillac",
    "model": "XT6",
    "year": 2024,
    "color": "Black",
    "bodyStyle": "SUV"
}
print(car)
car.update({"year":2022})
print(car)

# The pop() method removes the item with the specified key name
car = {
    "brand": "Cadillac",
    "model": "XT6",
    "year": 2024,
    "color": "Black",
    "bodyStyle": "SUV"
}
print(car)
car.pop("model")
print(car)

# The popitem() method removes the last inserted item from version 3.7
print(car)
car.popitem()
print(car)

# The del keyword removes the item with the specified key name
car = {
    "brand": "Cadillac",
    "model": "XT6",
    "year": 2024,
    "color": "Black",
    "bodyStyle": "SUV"
}
print(car)
del car["color"]
print(car)

# The del keyword can also delete the dictionary completely
print(car)
del car
# print(car)
# this will cause an error because "car" no longer exists. 

# The clear() method empties the dictionary
info = {
    "name": "Alex",
    "gender": "Male",
    "city": "New York",
    "age": 33,
    "grade": 3.3453,
    "fullTimeStudent": True
}
print(info)
info.clear();
print(info)

# the copy() method is used to make a copy of a dictionary
car = {
    "brand": "Cadillac",
    "model": "XT6",
    "year": 2024,
    "color": "Black",
    "bodyStyle": "SUV"
}
print(car)
newCar = car.copy()
print(newCar)

# the dict() method is used to make a copy of a dictionary
anotherCar = dict(car)
print(anotherCar)

# loop for dictionary
car = {
    "brand": "Cadillac",
    "model": "XT6",
    "year": 2024,
    "color": "Black",
    "bodyStyle": "SUV"
}

# Print all key names in the dictionary, one by one
for x in car:
    print(x)

print("-----------------------")
# Print all values in the dictionary, one by one
for x in car:
    print(car[x])

print("-----------------------")
# Print all keys in the dictionary, one by one
for x in car.keys():
    print(x)

print("-----------------------")
# Print all values in the dictionary, one by one
for x in car.values():
    print(x)

for x, y in car.items():
    print(x, y)

# A dictionary can contain dictionaries, this is called nested dictionaries

# Create three dictionaries, then create one dictionary that will contain the other three dictionaries
# 3 methods