
def food (item):
    for x in item:
        print(x)

# We can send any data types of argument to a function (string, number, list, dictionary etc.), and it will be treated as the same data type inside the function.

# Here we use argument as String type
food ("Banana")

# Here we use argument as List type
fruits = ["Orange", "Grapes", "Apple", "Strawberry"]
food(fruits)
