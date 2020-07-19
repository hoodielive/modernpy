columns = ['name', 'shares', 'price']
values = ['GOOG', 100, 490.1]

for colname, val in zip(columns, values):
    record = dict(zip(columns, values))
    print(colname, val)


names = ['IBM', 'YHOO', 'CAT']

for n, name in enumerate(names):
    print(n, name)


a = (1, 2, 3)
b = [4, 5]
c = [ *a, *b ]
d = ( *a, *b )


print(c) # list
print(d) # tuple

A = { 'name': 'GOOG', 'shares': 100, 'price': 490.1 }
B = { 'date': '6/11/2019', 'time': '9:45am' }

C = { **A, **B }

print(C)

e = (1, 2, 3)
f = (4, 5)


chash = {'x': 1, 'y': 2}

s = [1,2,3,4]
print(sum(s))
print(min(s))
print(max(s))

s = [False, True, True, False]

print(any(s))
print(all(s))