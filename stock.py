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

s = Stock('Google', 100, 490.10)
print(s.sell(25))