attributes = ['name', 'shares', 'price']

for attr in attributes:
    print(attr, '=', getattr('shares', attr))