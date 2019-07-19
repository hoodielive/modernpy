def huge_generator(num):
    for i in range(num):
        yield i
some_generator = huge_generator(32389283928392839)

for elem in some_generator:
    print(elem)
