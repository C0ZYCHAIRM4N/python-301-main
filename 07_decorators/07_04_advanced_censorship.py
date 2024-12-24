# Build on top of the censorship exercise and change your decorator function
# so that you can pass the words it should censor when decorating a function, e.g.:
# `@censor("shoot", "crab")` would censor the words "shoot" and "crab".

def censor(offensive_words):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            for word in offensive_words:
                result = result.replace(word, word[0] + '*' * (len(word) - 1))
            return result
        return wrapper
    return decorator

@censor(["shoot", "darn"])
def get_user_message():
    return input("Enter your message: ")

print(get_user_message())