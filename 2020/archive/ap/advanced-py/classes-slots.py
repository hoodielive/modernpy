from collections import namedtuple

class Stock():
    __slot__ = ('name', 'share', 'price')
    def __init__(self, name, share, price):
        self.name = name
        self.share = share
        self.price = price

Stock = namedtuple('Stock', ['name', 'shares', 'prices'])

class Player():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.health = 100

    def move(self, dx, dy):
        self.x += dx
        self.y += dy
        return (dx, dy)

    def damage(self, pts):
        self.health -= pts
        return pts


new_object = Player(4, 5)
print(new_object)

a = Player(2, 3)
b = Player(10, 20)
print(a.x)
print(b.x)
print(a.y)
print(b.y)

a.move(1,2)
a.damage(10)
