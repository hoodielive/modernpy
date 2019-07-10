from collections import namedtuple

class Stock(Object):
    __slot__ = ('name', 'share', 'price') 
    def __init__(self, name, share, price):
        self.name = name 
        self.share = share
        self.price = price

Stock = namedtuple('Stock', ['name', 'shares', 'prices'])

