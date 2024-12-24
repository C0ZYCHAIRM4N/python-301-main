# Write a decorator that literally decorates text output.
# Make it so the symbol it uses can be an argument to the decorator
#
# The output of a function that returns `"Hello"` that has been
# decorated like with `@decorate("*")` should look like this:
#
# ******************************
# Hello
# ******************************

def decorate(symbol):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            decoration = symbol * (len(result) + 4)
            return f"{decoration}\n{symbol} {result} {symbol}\n{decoration}"
        return wrapper
    return decorator

@decorate("*")
def get_user_message():
    return input("Enter your message: ")

print(get_user_message())
