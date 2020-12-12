class Human:
    species = "H. sapiens"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say(self, msg):
        print("{name}: {message}".format(name=self.name, message=msg))

    def sing(self):
        return 'yo.. yo.. microphone check.. one two.. one two..'

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
    def age(self, age):
        self._age = age

    @age.deleter
    def age(self):
        del self._age

if __name__ == '__main__':
    i = Human(name="Oso", age="33")
    i.say("Hi")
    i.say(i.get_species())
    
    print(Human.grunt())
    print(i.grunt())

    i.age = 42
    i.say(i.age)

    del i.age