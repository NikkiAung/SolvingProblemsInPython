# -------------------------------------------------------------------
# Global variables
# -------------------------------------------------------------------
decimalCode = 60

# =====> Add a line to create an integer variable named 'num' and
#        set it to 0


# -------------------------------------------------------------------
# Main program
# -------------------------------------------------------------------
# =====> Complete the line to take the input from the user and
# #      convert it to an integer
num = int(input('Enter a number: '))

# =====> Complete the if statement to check that the inputted number
#        is between 5 and 30.
#        Use two relational operators and one logical operator
if (( num >= 5) and      ( num <= 30 )):
    # =====> Complete the line to add 60 to num and assign the
    #        result to the variable decimalCode
    decimalCode = num + 60

    # =====> Complete the line to join strings together with concatenation
    print (str (num)  +   " is equal to "   +   chr (decimalCode))
else:
    # =====> Add a line to display an error message
    print('Invalid input')