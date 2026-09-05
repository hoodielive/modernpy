
x = [1, 3, 5, 7, 9]

sum_squared = 0

for i in range(len(x)):
    sum_squared += x[i] ** 2

sum_squared_2 = sum([y**2 for y in x])

x = [1, 2, 3, 4, 5, 6, 7, 8, 9]

even_squared = [y**2 for y in x if y%2==0]
print(even_squared)

squared_cube = [y**2 if y%2 == 0 else y**3 for y in x]

print(squared_cube)

L = ['blue', 'yellow', 'orange']

for i, val in enumerate(L):
    print("index is %d and value is %s" % (i, val))

x = [1, 2, 3, 4, 5, 6, 7, 8, 9]

dict_wick = { k: k**2 for k in x }
print(dict_wick)


text = """I need to count the number of word occurrences in a piece of text.
    How could I do that? Python provides us with multiple ways to do the same
thing. But only one way I find beautiful."""

word_count_dict = {}

for w in text.split(' '):
    if w in word_count_dict:
        word_count_dict[w] += 1
    else:
        word_count_dict[w] = 1

# A more elegant way:

from collections import defaultdict

word_count_dict = defaultdict(int)
for w in text.split(" "):
    word_count_dict[w] += 1
