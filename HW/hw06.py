'''
HW_Python_Condition_With_User_Input:

Step 1: Create a file name hw06.py inside the HW folder

Step 2: For temperature variable, we will use the feature "Python User Input". Inside the input function, type "Today's Temperature: ". so an user can put value of today's temperature in Terminal when the file is executed.

Step 3: Now create an User defined function name, "todaysTemperature" where the parameter is "temperature" . Inside the function, put below conditions sequentially.

Step 4: If the temperature is less than 32, then print "Freezing"

Step 5: If the temperature is less than 55, then print "Pleasant"

Step 6: If the temperature is less than 73, then print "Getting Warmer"

Step 7: If the temperature is greater than 101, then print "Very Hot"

Step 8: And finally print "Please put a valid temperature" where no condition present.

Step 9: In the above 5 conditions, use the appropriate keyword like if, elif, else to execute today's Temperature condition.

Step 10: Now Call the function with the parameter and Run the code. Type today's temperature in the Termial, and find the correct condition of the today's weather.

Step 11: Please organize the code

Step 12: Copy the code and paste it below.
'''

temperature = input("Today's temperature")

if temperature <32:
    print( "Freezing")
elif temperature <55:
    print( "Pleasant")