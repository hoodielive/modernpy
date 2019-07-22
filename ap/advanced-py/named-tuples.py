from collections import namedtuple 

Stock = namedtuple('Stock', ['name', 'shares', 'price'])
s = Stock('Goog', 100, 490.1)
print(s)

import typing 
# alternate formation of a namedtuple
class Stock(typing.NamedTuple):
    name: str
    shares: int 
    price: float

s = Stock('Google', 100, 490.1) 
print(s.name)
print(s.price)
print(s.shares)

s = Stock(1, 'a lot', 3)
print(s.name)
