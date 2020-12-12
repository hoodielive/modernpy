# Working with files.

with open('possible.csv', 'rt') as f:
    for lines in f:
        print(lines)