import typing

a = ('apple', 1, 'Amber', 2.5)
fruit, integer, sister, afloater = a

print(fruit)
print(integer)
print(sister)
print(afloater)
print(a)


b = ()

class Stock(typing.NamedTuple):
    name: str
    shares: int
    price: float


stock = Stock(3, 100, 490.1)
print(stock)
