for x in range(10):
    print(f"10^{x} == {10**x:10d}")


evens = []
for i in range(10):
    if i % 2 == 0:
        evens.append(i)

print(evens)

# Shorter with comprehensions:

consider = [i for i in range(10) if i % 2 == 0]
print(consider)

# Other idioms
i = 0
for element in ['one', 'two', 'three']:
    print(i, element)
    i += 1

for i, element in enumerate(['one', 'two', 'three']):
    print(i, element)
    i += 1

for i, element in enumerate(['one', 'two', 'three']):
    print(i, element)

for items in zip([1, 2, 3], [4, 5, 6]):
    print(items)

for items in zip(*zip([1, 2, 3], [4, 5, 6])):
    print(items)

for items in zip([1, 2, 3, 4], [1, 2]):
    print(items)

first, second, third = "foo", "bar", 100
print(first)
print(second)
print(third)

first, *inner, last  = 0, 1, 2, 3
print(first, *inner, last)

(a, b), (c, d) = (1, 2), (3, 4)

print(a, b, c, d)

print({
    1: ' one',
    2: ' two',
    3: ' three'
})

squares = { number: number ** 2 for number in range(100) }
print(squares)

person = { 'first_name': 'Jon', 'last_name': 'Doe' }
items = person.items()
person['age'] = 42
print(items)

print({ number: None for number in range(5) }.keys())
print({ str(number): None for number in range(5).keys()})
print({ str(number): None for number in reversed(range(5)).keys()})
