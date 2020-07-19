portfolio = [
    ('Goog', 100, 490.1),
    ('IBM', 50, 91.1),
    ('CAT', 150, 83.44)
]

print(portfolio[0])

print(portfolio[1])


a = { 'IBM', 'AA', 'AAPL' }

names = ['IBM', 'YHOO', 'IBM', 'CAT', 'MSFT', 'CAT', 'IBM']

unique_names = set(names)

print(unique_names)

members = set()

item = ('Mephisteles', 'Hypnos', 'Reperia')
members.add(item)
print(members)

if item in members:
    print(item)

prices = {
    ('GOOG', '2019-01-20') : 513.25,
    'CAT'  : 87.22,
    'IBM'  : 93.37,
    'MSFT' : 44.12
}

p = prices.get('AAPL', 0.0)
prices['HPE'] = 37.42

if 'name' in prices:
    print('It is')
else:
    print('IT is not')


print(prices['GOOG', '2019-01-20'])

print(prices.keys())
print(prices.values())
print(prices.items())

# Tabulation of total shares of each stock

portfolio = [
    ('Goog', 100, 490.1),
    ('IBM', 50, 91.1),
    ('CAT', 150, 83.44)
]


from collections import Counter, defaultdict, deque
total_shares = Counter()

for name, shares, price in portfolio:
    total_shares[name] += price

print(total_shares)

history = deque(maxlen=4)

prices = [
    ['GOOG', 490.1, 485.25, 487.5],
    ['IBM', 91.5],
    ['HPE', 13.75, 12.1, 13.25, 14.2, 13.5],
    ['CAT', 52.5, 51.2]
]

for name, *values in prices:
    print(name, values)