y = iter([1, 2, 3])
print(next(y))
print(next(y))
print(next(y))

j = reversed([7, 8, 9])
print(next(j))
print(next(j))
print(next(j))

def file_sigs():
    sigs = [('jpeg', 'FF D8 FF EO'),
            ('png', '89 50 4E 47 0D 0A 1A 0A'),
            ('gif', '47 49 46 38 37 61')
           ]
    for s in sigs:
        yield s

fs = file_sigs()
print(next(fs))
print(next(fs))
print(next(fs))
