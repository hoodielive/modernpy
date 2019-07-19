a = [2,3,[100,101],4]

print(id(a))

b = list(a)
b = a
print(id(b))

print(a is b)