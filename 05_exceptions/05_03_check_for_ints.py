# Create a script that asks a user to input an integer, checks for the
# validity of the input type, and displays a message depending on whether
# the input was an integer or not.
# The script should keep prompting the user until they enter an integer.
while True:
    try:
        num = int(input("Enter number: "))
        print(f"You entered the number: {num}")
        break  # Exit the loop if the input is a valid number
    except ValueError:
        print("That's not a valid number. Please try again.")
