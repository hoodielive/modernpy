#!/usr/bin/env python3

class Stock():
    __slots__ = ('name', 'shares', 'price')
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

s = Stock('Goog', 100, 490.1)
print(s.name)
print(s.shares)
print(s.price)

