# Create a decorator that censors potentially offensive words from a text.
# For example, assuming that "shoot" was considered an offensive word:
# A function that would normall return this text:
#    "I bumped my toe! Shoot!"
# Would, after decorating it with `@censor()`, return:
#    "I bumped my toe! S****!"

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

