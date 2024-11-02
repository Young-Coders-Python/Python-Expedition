# Here id and name are List
id = [213, 976, 901, 388]
name = ["Joe", "Rejina", "Brian", "Michael"]
# The zip object yields n-length tuples
object = list(zip(id, name))
print(object)

# you can also print it directly, will provide same result
print(list(zip(id, name)))

# also you can add other variable inisde the zip function
print(list(zip(id, name, "AABA")))
