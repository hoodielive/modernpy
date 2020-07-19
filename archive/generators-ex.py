def gen():
    print('--start')
    yield 1
    print('--middle')
    yield 2
    print('--stop')

g = gen()

print(g)

if 5 > 3:
    print(next(g))
    print(next(g))

    # get a iteration error
    print(next(g))
else:
    print('I cant')

#print(next(g))