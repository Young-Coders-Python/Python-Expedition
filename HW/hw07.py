
'''
HW_Python_Nested_If:

Step 01: Create a file name hw07.py inside the HW folder

Step 02: Hemoglobin A1C is measured to determine - you are diabetic or not. Now create an User defined function name, "diabeticCondition" where the parameter is "hbA1c" . Inside the function, put below conditions sequentially.

Step 03: If your hbA1c value is more than 6.4, the outcome will be "I am a diabetic patient".

Step 04: If your hbA1c value is less than or equal to 6.4, follow below 2 conditions inside it. If hbA1c >= 5.7, the outcome will be "I am a pre-diabetic patient". If hbA1c < 5.7, the outcome will be "I am a healthy person".

Step 05: And finally print "Please add a valid hbA1c value" where no condition present.

Step 06: In the above conditions, use an appropriate keyword like if, elif, or else to find out your health condition.

Step 07: Now Call the function with the argument and Run the code.

Step 08: Please organize the code.

Step 09: Push the code to GitHub and add the link below.

'''

def diabeticCondition(hbA1c):
    if hbA1c > 6.4:
        print("I am a diabetic patient.")
    elif hbA1c <=6.4:
        if hbA1c >= 5.7:
            print("I am a pre-diabetic patient.")
        elif hbA1c < 5.7:
            print("I am a healthy person.")  
    else:
        print("Please add a valid hbA1c value.") 

diabeticCondition(5.6)  