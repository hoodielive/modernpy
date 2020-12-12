import csv
import json

# Working with files.

with open('possible.csv', 'rt') as f:
    head = csv.reader(f, delimiter="\t")
    next(head)
    for lines in enumerate(f):
        print(lines)

contents = {"aa": 12, "bb": 21}

with open('darling.txt', 'wt') as f:
    f.write(str(contents)) # writes a string to a file.

with open('revolving_door.txt', 'wt') as f:
    f.write(json.dumps(contents)) # writes an object to a file.

with open('revolving_door.txt', 'r+') as file:
    contents = json.load(file)

print(type(contents))
content_values = contents.values()

print(content_values); print(contents)

# Fundamental Abstraction called the Iterable.
# An iterable is an object that can be treated as a sequence.
# The object returned by the range function, is an iterable.

filled_dict = {"one": 1, "two": 2, "three": 3}
our_iterable = filled_dict.keys()
print(our_iterable)

for i in our_iterable:
    print(i)