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