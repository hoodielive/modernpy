class Stock(object):
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    def cost(self):
        return self.shares * self.price

    def sell(self, nshares):
        return self.shares -= nshares

    def read_portfolio(self):
        '''
        Read a csv file of stock into a list of Stocks
        '''
        import csv
        portfolio = []
        with open(filename) as f:
            rows = csv.reader(f)
            headers = next(rows)
            for row in rows:
                record = Stock(row[0], int(row[1]), float(row[2]))
                portfolio.append(record)
        return portfolio



s = Stock('GOOG', 100, 490.1)
print(s.name)
print(s.shares)
print(s.price)
print(s.cost())