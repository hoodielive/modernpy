import csv
from collections import Counter

class ReadPortfolio:
    def __init__(self, filename):
        self.filename = filename

    def read_portfolio(self):
        portfolio = []
        with open(self.filename) as f:
            rows = csv.reader(f)
            headers = next(rows)
            for row in rows: 
                record = {
                    'name': row[0],
                    'shares': int(row[1]), 
                    'price': float(row[2]), 
                }
                portfolio.append(record)
        return portfolio

def the_art_of_counting(name):
    totals = Counter()
    doctor = ReadPortfolio('data/portfolio.csv')
    for s in doctor.read_portfolio():
        totals[s['name']] += s['shares']
    return totals[name]


the_art_of_counting('data/portfolio.csv')