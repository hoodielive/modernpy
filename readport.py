import csv
from collections import Counter

def read_portfolio(filename):
    portfolio = []
    with open(filename) as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows: 
            record = {
                'name': row[0],
                'shares': int(row[1]), 
                'price': float(row[2]), 
            }
            portfolio.append(record)

        totals = Counter()
        for s in portfolio:
            totals[s['name']] += s['shares']
        print(totals['IBM'])

    return portfolio

print(read_portfolio('data/portfolio.csv'))

