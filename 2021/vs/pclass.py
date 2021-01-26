class Game:
    def reset(self):
        self.x = 0
        self.y = 0


a = Game()
a.x = 5
a.y = 4
print(a.x, a.y)
a.reset()
print(a.x, a.y)
