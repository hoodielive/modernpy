class Dice1:
    def __init__(self, seed=None):
        self.__rng = random.Random(seed)
        self.roll
    def roll(self):
        self.dice = (self.__rng.randint(1, 6)),
                     self.__rng.randint(1, 6)
        return self.dice

class Die:
    def __init__(self, rng):
        self.__rng = rng
    def roll(self):
        return self.__rng.randint(1, 6)

class Dice2:
    def __init__(self, seed=None):
        self.__rng = random.Random(seed)
        self.__dice = [Die(self.__rng) for _ in range(2)]
        self.roll()
    def roll(self):
        self.dice = tuple(d.roll() for d in self.__dice)
        return self.dice
