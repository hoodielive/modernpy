a = [1,2,3,4,5]

b = [2*x for x in a]

print(b)

# filter

c = [2*x for x in a if x > 3]
print(c)

# Collecting the values of a specific field

portfolio = [
    ('GOOG', 100, 490.1),
    ('IBM', 50, 91.1),
    ('CAT', 150, 83.44)
]

a_tuple = ('a', 'b', 'c')

print(a_tuple[0])

stocknames = [s[0] for s in portfolio ]
print(stocknames)

lumna = [s for s in portfolio if s[2] > 100 and s[1] > 50 ]
print(lumna)

cost = sum([s[1] * s[2] for s in portfolio])
print(cost)


