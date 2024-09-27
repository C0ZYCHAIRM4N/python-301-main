# Write a script that takes in two numbers from the user and calculates the quotient.
# Use a try/except statement so that your script can handle:
#
# - if the user enters a string instead of a number
# - if the user enters a zero as the divisor
#
# Test it and make sure it does not crash when you enter incorrect values.
numbers = []

try:
    for i in range(2):
        num = int(input("enter 2 numbers: "))
        numbers.append(num)
    quotient = numbers[0] / numbers[1]
    print(quotient)
except ValueError:
    print("you didn't enter a number!")
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")



    


    








