class Player():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.health = 100

    def move(self, dx, dy):
        self.dx += dx
        self.dy += dy

    def damage(self, pts):
        self.health -= pts


a = Player(2,3)
print(a.move(3, 2))