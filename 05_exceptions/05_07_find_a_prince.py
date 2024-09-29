# Write a custom exception  that inherits from `Exception()`
# Open and read in the content of the book `.txt` files in the `books/` folder
# like you did in the previous exercise.
# Raise your `PrinceException()` if the first 100 characters of a book
# contain the string "Prince".


class PrinceException(Exception):
    pass



try:
    file_in = open(r"C:\Users\speng\Downloads\python-301-main\python-301-main\05_exceptions\books\war_and_peace.txt", 'r', encoding='utf-8')
    contents = file_in.read(100)
    if "Prince" in contents:
        raise PrinceException("The string 'Prince' was found in the first 100 characters of the book.")
except UnicodeDecodeError as e:
    print("UnicodeDecodeError: whoops")
except PrinceException as e:
    print(e)
finally:
    file_in.close()

 


