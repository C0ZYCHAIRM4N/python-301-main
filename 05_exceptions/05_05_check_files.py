# Read in the first number from `integers.txt`
# and perform a calculation with it.
# Make sure to catch at least two possible Exceptions (`IOError` and `ValueError`)
# with specific `except` statements, and continue to do the calculation
# only if neither of them applies.

file_name = 'integers.txt'
try:
    file_in = open(r"C:\Users\speng\Downloads\python-301-main\python-301-main\05_exceptions\integers.txt", 'r')
    first_number = file_in.readline().strip()
    first_number = int(first_number)
    calculation = first_number + 2
    print(calculation)
except IOError as e:
    print("IOError occured")
except ValueError as e:
    print("value error") 

    

