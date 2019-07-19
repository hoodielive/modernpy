d = { i: i * 2 for i in range(10) }

print(d)

s = { i for i in range(10) }

print(s)

print([(x,y) for x in range(5) for y in range(3)])


points = []
for x in range(5):
    for y in range(3):
        points.append((x,y))
print(points)

values = [ x / (x-y) for x in range(100) if x > 50 for y in range(100) if x - y != 0 ]

print(values)

m = map(ord, 'turtles all the way down')

print(m)
print(isinstance(m, map))


# advanced comprehension(s)
oldlist = [1,3,4]

def somefunc(elem):
    return elem

new_list = [] 
for elem in oldlist:
    new_list.append(somefunc(elem))

print(new_list)

print(somefunc(new_list))

newlist = [somefunc(elem) for elem in oldlist]

print(newlist)

zlist = [] 
xlist = [1,2,3, 'a']
ylist = [4,5,6, 'b']

def func(a, b):
    return (a, b) 

for x in xlist:
    for y in ylist: 
        zlist.append(func(x,y))

new_zlist = [func(x, y) for x in xlist for y in ylist]

print(new_zlist)

zlist = [] 

def cond(x, y):
    return (x, y)

def f(a, b):
    return (a, b)

new_zlist = [f(x, y) for x in xlist for y in ylist if cond(x, y)]

print(new_zlist)
