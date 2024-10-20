# A set is a collection which is unordered [unindexed], unchangeable*
# Sets are written with curly brackets
# Set items can be of any data type [String, int, boolean, float, list, tuple]
car = {"Toyota", "Ford", 3224, 3.5345, False}
print(car)
print(type(car))
print(len(car))

# Duplicates Not Allowed in set
car = {"Toyota", "Ford", 3224, 3.5345, False, "Toyota", 3224}
print(car)

# The values True and 1 are considered the same value in sets, and are treated as duplicates
# The values False and 0 are considered the same value in sets, and are treated as duplicates
car = {"Toyota", True, 1, 0, "Ford", 3224, 3.5345, False, "Toyota", 3224,  True}
print(car)

# we can use the set() constructor to make a set.
# # note the double round-brackets
newSet = set(("Toyota", "Ford", 3224, 3.5345, False))
print(newSet)

# Set is unindexed, so you can't call by index no
# how to access set?
brand = {"Toyota", "Cadillac", "Ford", "Honda", "Toyota", "Nissan", "GMC"}
for x in brand:
    print(x)

print("Toyota" in brand)
print("Koyota" in brand)
print("Ford" not in brand)
print("Cord" not in brand)

# Set items are unchangeable, meaning that we cannot change the items after the set has been created. Once a set is created, you cannot change its items, but you can remove items and add new items
brand = {"Toyota", "Cadillac", "Ford", "Honda", "Toyota", "Nissan", "GMC"}
# To add one item to a set, we use the add() method
brand.add("BMW")
print(brand)

# To add items from another set into the current set, use the update() method.
# update() will exclude any duplicate items.
brand1 = {"Toyota", "Honda", "Nissan", "Lexus", "Acura"}
print(brand1)
brand2 = {"Ford", "GMC", "Cadillac", "Tesla", "Lexus"}
print(brand2)
brand1.update(brand2)
print(brand1)

# To add items from another list or tupple into a set, we can also use the update() method.
brand = {"Toyota", "Honda", "Nissan", "Lexus", "Acura"}
print(brand)
brandUSA = ["Ford", "GMC", "Cadillac", "Tesla"] # This is a list
print(brandUSA)
brand.update(brandUSA)
print(brand)

brand = {"Toyota", "Cadillac", "Ford", "Honda", "Toyota", "Nissan", "GMC"}
# To remove an item in a set, use the remove(), or the discard() method.
# If the item which is removed, does not exist, remove() will raise an error.
brand.remove("Toyota")
print(brand)

# remove() vs discard()
# If the item to remove does not exist, discard() will NOT raise an error.
brand.discard("GMC")
print(brand)

# Remove a random item by using the pop() method
brand = {"Toyota", "Cadillac", "Ford", "Honda", "Nissan", "GMC"}
brand.pop()
print(brand)

# The clear() method empties the set
brand = {"Toyota", "Cadillac", "Ford", "Honda", "Nissan", "GMC"}
brand.clear()
print(brand)

# The del keyword will delete the set completely
brand = {"Toyota", "Cadillac", "Ford", "Honda", "Nissan", "GMC"}
del brand
# print(brand)

# The union() method returns a new set with all items from both sets.
# Join set1 and set2 into a new set:
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2)
print(set3)

# You can use the | operator instead of the union() method
# Use | to join two sets:
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set3 = set1 | set2
print(set3)

# Join multiple sets with the union() method:

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}

myset = set1.union(set2, set3, set4)
print(myset)

# Use | to join two sets:
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}

myset = set1 | set2 | set3 |set4
print(myset)

# Join a set with a tuple:
x = {"a", "b", "c"}
y = (1, 2, 3)

z = x.union(y)
print(z)
# The  | operator only allows you to join sets with sets, and not with other data types like you can do with the  union() method.

# union() will exclude any duplicate items.

# The intersection() method will return a new set, that only contains the items that are present in both sets.
# Join set1 and set2, but keep only the duplicates:
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.intersection(set2)
print(set3)

# we can use the & operator instead of the intersection() method
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1 & set2
print(set3)
# The & operator only allows you to join sets with sets, and not with other data types like you can with the intersection() method.

# Keep the items that exist in both set1, and set2:

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set1.intersection_update(set2)
print(set1)

# Join sets that contains the values True, False, 1, and 0, and see what is considered as duplicates:

set1 = {"apple", 1,  "banana", 0, "cherry"}
set2 = {False, "google", 1, "apple", 2, True}

set3 = set1.intersection(set2)

print(set3)

# The difference() method will return a new set that will contain only the items from the first set that are not present in the other set.

# Keep all items from set1 that are not in set2:

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.difference(set2)

print(set3)

# Use - to join two sets:

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1 - set2
print(set3)

# Use the difference_update() method to keep the items that are not present in both sets:

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set1.difference_update(set2)

print(set1)

# Keep the items that are not present in both sets:

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.symmetric_difference(set2)

print(set3)

# You can use the ^ operator instead of the symmetric_difference() method, and you will get the same result.
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1 ^ set2
print(set3)
# The ^ operator only allows you to join sets with sets, and not with other data types like you can with the symmetric_difference() method.

# Use the symmetric_difference_update() method to keep the items that are not present in both sets:
# The symmetric_difference_update() method will also keep all but the duplicates, but it will change the original set instead of returning a new set.
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set1.symmetric_difference_update(set2)

print(set1)