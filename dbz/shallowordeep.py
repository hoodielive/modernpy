a = [2,3,[100,101],4]

print(id(a))

b = list(a)
b = a
print(id(b))

print(a is b)

import copy

b = copy.deepcopy(a) # this is the only safe way to copy something

print(a is b)

a[2].append(102)
print(a[2])
print(b[2])