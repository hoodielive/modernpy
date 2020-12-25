class Mpungos:
    def __init__(self, lucero, zarabanda, kengue, ngurufinda):
        self.lucero = lucero
        self.zarabanda = zarabanda
        self.kengue = kengue
        self.ngurufinda = ngurufinda

    def LuceroMundo(self):
        return dict(self.lucero)

    def Zarabanda(self):
        return tuple(self.zarabanda)

    def YaYaKengue(self):
        return list(self.kengue)

    def Ngurufinda(self):
        return set(self.ngurufinda)

lc = Mpungos(
    {'name': 'Lucero Mundo', 'age': 'Depends on ceremony', 'power': 'Doing/Undoing'}, 
    ('Power', 'Removal of Obstacles'),
    ['Prophecy', 'Creation', 'Destruction', 'Expansion', 'Mental Clarity'],
    ('herbs', 'Witchcraft', 'Ase')
)

print(lc.LuceroMundo())
print(lc.Zarabanda())
print(lc.YaYaKengue())
print(lc.Ngurufinda())