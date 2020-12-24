# Decorator lesson.

def identify(f):
    return f

# So a decorator is a function that takes another
# function as an argument and replaces it with a new
# modified function.

@identity
def foo():
    return 'bar'