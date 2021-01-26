def check_is_admin(username):
    def wrapper(*args, **kwargs):
        if kwargs.get('username') != 'admin':
            raise Exception("This user is not allowed to get food.")
        return f(*args, **kwargs)
    return wrapper



func = lambda a,b : a + b
print(func(4, 5))


print(check_is_admin('Devil'))