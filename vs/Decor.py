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

def check_is_admin(username):
    def wrapper(*args, **kwargs):
        if kwargs.get('username') != 'admin':
            raise Exception("This user is not allowed to get food.")
        return f(*args, **kwargs)
    return wrapper

class Store(object):
    def __init__(self, storage):
        self._storage = storage

    @check_is_admin
    def get_food(self, username, food):
        return self._storage.get(food)

    @check_is_admin
    def put_food(self, username, food):
        self._storage.put(food)
    

user01 = Store('Oya')
print(user01.get_food('Oya', 'pizza'))

# If you stare into an abyss, it too will stare into you. 

