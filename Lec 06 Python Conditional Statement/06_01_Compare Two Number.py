'''
Conditional Statements allow the program to behave differently based on condition. 
Below keywords are used
Example: if, else, elif 

In First condition, we have to always use 'if' keyword.
now, if the condition is true, then interpreter will execute the statement inside that condition and the rest will be skipped.

if the condition is false, the statement inside the condition will be skipped

We use 'if' as first condition 'elif' as second condition and else as last condition. 
When we write 'else' keyword, no condition is necessary to write
Whatever you want to print, it will be printed in else block/body. 
either it is true or false, correct or incorrect, logical or not logical, it doesn't matter.

But if we wish to write a second condition , we have to use 'elif' with condition 

The last condition is generally "else", but not always
'If' condition and 'else' condition is used one time in the execution
first condition 'if', last condition generally 'else', but not always, 
'elif' can also be is used with condition at the end.

if there are more condition, you can use more than one 'elif' condition
'''

a = 70
b = 60

if a>b:
    print(a, "is greater than", b)
elif a<b:
    print(a, "is smaller than", b)
elif a==b:
    print(a, "is equal to", b)
else:
    print("The system failed to execute this order")