class Human:
    species = "H. sapiens"

    def __init__(self, name):
        self.name = name
        self._age = 0

    def say(self, msg):
        print("{name}: {message}".format(name=self.name, message=msg))

    def sing(self):
        return 'yo..yo..yo Mind Chekka!'

    @classmethod
    def get_species(cls):
        return cls.species

    @staticmethod
    def grunt():
        return "*grunt*"

    @property
    def age(self):
        return self._age
    
    @age.setter
    def age(self):
        self._age = age

    @age.deleter
    def age(self):
        del self._age


if __name__ == '__main__':
    i = Human(name="Larry")
    i.say("hi")
    j =  Human("Enilo")
    j.say("hello")

    print(Human.grunt())
    print(Human.grunt())

class SuperHero(Human):
    def __init__(self, name, movie=False, superpowers =
                 ["super strength", "bulletproofing"]):
        self.fictional = True
        self.movie = movie
        self.superpowers = superpowers
        super().__init__(name)

    def sing(self):
        return 'Dun, dun, Dun!'

    def boast(self):
        for power in self.superpowers:
            print("I Will wield the power of {pow}".format(pow=power))

if __name__ == '__main__':
    sup = SuperHero(name="Tick")

    if isinstance(sup, Human):
        print("I am human.")
    if type(sup) is SuperHero:
        print('I am a superhero')

    print(SuperHero.__mro__)
    print(sup.get_species())
    print(sup.sing())
    sup.say("Spoon")
    sup.boast()

    print(sup.age)
    print('Am I Oscar elgible?' + str(sup.movie))


