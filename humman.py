class Human:
    species = "H. Sapiens"

    def __init__(self, name):
        self.name = name
        self._age = 0

    def say(self, msg):
        print("{name}: {message}".format(name=self.name, message=msg))

    def sing(self):
        return 'yo... yo... microphone check... one two... one two...'

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
        del self.age


if __name__ == '__main__':
    i = Human(name="Conscire")
    i.say("hi")
    j = Human("Osa")
    j.say("hello")

    i.say(i.get_species())
    j.say(j.get_species())

    print(Human.grunt())
    print(i.grunt())

    i.age = 42
    i.say(i.age)
    j.say(j.age)

    del i.age
