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
    if username != 'admin':
        raise Exception("This user is not allowed to get food.")

class Store(object):
    def __init__(self, storage):
        self._storage = storage

    def get_food(self, username, food):
        check_is_admin(username)
        return self._storage.get(food)

    def put_food(self, username, food):
        check_is_admin(username)
        self._storage.put(food)
    

user01 = Store('admin')
print(user01.get_food('Satana', 'pizza'))

