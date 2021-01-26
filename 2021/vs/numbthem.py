# Assertion 
import csv

a_list_of_tuples = [(2, 2, 4), (9, 2, 11), (2, 3, 5)]
# functional program; because it does not manage state, 
# rather it returns a value and dies.

def add(x, y):
    return x * y


if iter(a_list_of_tuples) == True:
    print("It is iterable.")

try:
    for x, y, z in a_list_of_tuples:
        if add(2, 2, 3) == 4:
            print(f"add({x}, {y}) == {z}")
except TypeError:
    print("Messed up.")
finally:
    print("Closing her out.")


with open("Nzambi.txt", "r+") as f:
    head = csv.reader(f)
    next(head)
    for words in f:
        words = words.split(",")
        cleanup = words[3].strip('\n')
        print(type(words[2]))
        print(words)