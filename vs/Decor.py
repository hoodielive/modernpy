# Decorator lesson.

def identify(f):
    return f

# So a decorator is a function that takes another
# function as an argument and replaces it with a new
# modified function.

@identify
def foo():
    return 'bar'

foo = identify(foo)

# A useless decorator that does nothing:

_functions = {}
def register(f):
    global _functions
    _functions[f.__name__] = f
    return f

@register 
def foo(): return 'bar'