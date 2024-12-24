# Write a decorator function that wraps text output into quotes, e.g.:
# Hello world! ----> "Hello World!"
# You can use it to create quotes from text output.

def quote_wrap(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return f'"{result}"'
    return wrapper

@quote_wrap
def say_hello():
    return "Hello world!"

print(say_hello())  
