class GiveMeACallBitch:
    def __init__(self, name, trait):
        self.name = name
        self.trait = trait

    def define_trait(self, trait):
        return trait

    def specify_name(self, name):
        if name is name:
            return name
        else:
            return 0 

    def getter(self, name, trait):
        ... 

person = GiveMeACallBitch("Larry", "Bad Mama Jama")

print(person.name, person.trait)

person2 = GiveMeACallBitch("Keith", "Cool dude")

print(person2.name, person2.trait)


def gen123():
    yield 1
    yield 2
    yield 3

print(gen123())


