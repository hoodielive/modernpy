class Stock(object):
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares 
        self.price = price

    def cost(self):
        return self.shares * self.price 
        
    def sell(self, nshares):
        nshares -= self.shares
        return nshares

    def read_portfolio(self, file):
        file = open('./data/portfolio.csv', 'rt')
        for s in file:
            print('%10s %10d %10.2f' % (s.name, s.shares, s.price)

s = Stock('Google', 100, 490.10)
s.read_portfolio('./data/portfolio.csv')