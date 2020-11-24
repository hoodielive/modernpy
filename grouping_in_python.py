from itertools import groupby

# List of tuples
items = [(1, "a"), (3, "q"), (2, "c"), (2, "x"), (1, "z")]

for key, group in groupby(sorted(items), lambda x: x[0]):
    print(key)
    for tuple in group:
        print(tuple)
    print("------------------")


