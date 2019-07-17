import dis

a = 2
b = 3
c = 'hello'

print(a.__add__(b))

print(c.__len__())

def f(x, y):
    return x + y


dis.dis(f)