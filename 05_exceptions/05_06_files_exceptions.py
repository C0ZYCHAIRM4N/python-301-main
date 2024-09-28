# In this exercise, you will practice both File I/O as well as using Exceptions
# in a real-world scenario.
#
# This folder contains another folder called `books/` that contains three text files
# of books from Project Gutenberg:
# 1. war_and_peace.txt
# 2. pride_and_prejudice.txt
# 3. crime_and_punishment.txt
#
# 1) Open `war_and_peace.txt`, read the whole file content and store it in a variable
# 2) Open `crime_and_punishment.txt` and overwrite the whole content with an empty string
# 3) Loop over all three files and print out only the first character each. Your program
#    should NEVER terminate with a Traceback.
#     a) Which exception can you expect to encounter? Why? -------unicodedecodeerror
#     b) How do you catch it to avoid the program from terminating with a traceback? 

try:
    file_in = open(r"C:\Users\speng\Downloads\python-301-main\python-301-main\05_exceptions\books\war_and_peace.txt", 'r')
    contents = file_in.read()
except UnicodeDecodeError as e:
    print(f"Error reading file: {e}")
finally:
    try:
        file_in.close()
    except NameError:
        pass

# Clear the contents of the file
with open(r"C:\Users\speng\Downloads\python-301-main\python-301-main\05_exceptions\books\war_and_peace.txt", 'w') as war_and_peace:
    war_and_peace.write("")

