# # Loop is a programming structure that repeats a sequence of instructions until a specific condition is met.
# Python has two primitive loop commands: while loops, for loops

"""
initialization block
while Conditional block:
    statement to print
    incremental or decremental block
"""

# Initilization block: i=1
# Conditional block: i<10
# Incremental or Decremental block


# Incremental block: i+=1, incremented by 1, you can also write i = i+1
# Incremental block: i+=2, incremented by 2, you can also write i = i+2
# Incremental block: i+=3, incremented by 3, you can also write i = i+3

# Decremental block: i-=1, decremented by 1, you can also write i = i-1
# Decremental block: i-=2, decremented by 2, you can also write i = i-2
# Decremental block: i-=3, decremented by 3, you can also write i = i-3

# This is not mandatory to start the initialization block from 0
# This is not mandatory to increment by 1

# incremental
i = 1
while i<10:
    print(i)
    i+=2
print("Porgram End")
# 1, 3, 5, 7, 9

i = 0
while i<5:
    print(i)
    i+=1
print("Porgram End")

j=1
while j<8:
    print(j)
    j+=2
# 1, 3, 5, 7
print("Porgram End")

# decremental
i=20
while i>6:
    print (i)
    i-=3
print("Porgram End")
# 20, 17, 14, 11, 8, 