# Decorator lesson.
# So a decorator is a function that takes another
# function as an argument and replaces it with a new
# modified function.

def identify(f):
    return f

@identify
def foo():
    return 'bar'

foo = identify(foo)
print(foo())
# A useless decorator that does nothing:

_functions = {}
def register(f):
    global _functions
    _functions[f.__name__] = f
    return f

@register 
def foo(): return 'bar'

def check_is_admin(username):
    def wrapper(*args, **kwargs):
        if kwargs.get('username') != 'admin':
            raise Exception("This user is not allowed to get food.")
        return f(*args, **kwargs)
    return wrapper

def is_admin(f):
    def wrapper(*args, **kwargs):
        if kwargs.get('username') != 'admin':
            raise Exception("I said this user is not allowed to eat.")
        return f(*args, **kwargs)
    return wrapper

@is_admin
def foobar(username="Someone"):
    """Do some crazy shii""" 
    pass

class Store(object):
    @check_is_admin
    def get_food(self, username, food):
        return self._storage.get(food)

    @check_is_admin
    def put_food(self, username, food):
        self._storage.put(food)
    

user01 = Store()
print(user01.get_food('Oya', 'pizza'))

# If you stare into an abyss, it too will stare into you. 


# Um.. okay. 
#from functools import update_wrapper
#
#WRAPPER_ASSIGNMENTS = ('__module__', '__name__', '__qualname__', '__doc__', '__annotations__')
#WRAPPER_UPDATES = ('__dict__',)
#
#def update_wrapper(wrapper, wrapped, 
#                    assigned=WRAPPER_ASSIGNMENTS, 
#                    updated=WRAPPER_UPDATES):
#    wrapper.__wrapped__ = wrapped
#
#    for attr in assigned:
#        try:
#            value = getattr(wrapped, attr)
#        except AttributeError:
#            pass
#        else: 
#            setattr(wrapper, attr, value)
#    
#    for attr in updated:
#        getattr(wrapper, attr).update(getattr(wrapped, attr, {}))
#        # Return the wrapper so this can be used as a decorator via partial()
#        return wrapper
#
#foobar = functools.update_wrapper(is_admin, foobar)
#
#print(foobar.__doc__)
#print(foobar.__name__)