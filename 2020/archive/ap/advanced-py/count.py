from collections import Counter,defaultdict,deque

import typing 

class Stock(typing.NamedTuple):
    name: str
    shares: int
    prices: float

s = Stock('IBM', 100, 490.1)

portfolio = [
        ('GOOG', 100, 490.1),
        ('IBM', 50, 91.1),
        ('CAT', 150, 83.44),
        ('IBM', 100, 45.23),
        ('GOOG', 75, 572.45),
        ('AA', 50, 23.15),
]

total_shares = Counter()
for name, shares, price in portfolio:
    total_shares[name] += shares 

print(total_shares['IBM']) 

holdings = defaultdict(list) 
for name, shares, price in portfolio:
    holdings[name].append((shares, price))
print(holdings)
print(holdings['IBM'])

history = deque(maxlen=N)
with open(filename) as f:
    for line in f:
        history.append(line)
