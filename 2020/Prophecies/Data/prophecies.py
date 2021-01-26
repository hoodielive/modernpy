
dreams = {'car': 'audi', 'house': 'mansion', 'vacation': 'maui'}

for i, war in enumerate(dreams.items()):
    print(i, war)

try:
    raise SyntaxError("Hey Bitch!")
except SyntaxError as e:
    print(e)

finally:
    print("We are moving on now.")