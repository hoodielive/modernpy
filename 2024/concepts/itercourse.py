filled_dict = { "one": 1, "two": 2, "three": 3 }
our_iterable = filled_dict.keys()

# We can loop over it.
for i in our_iterable:
    print(i)

our_iterator = our_iterable
print(list(our_iterator))

def add(x, y):
    print("x is {} and y is {}".format(x, y));
    return x + y

a = add(5, 6)
print(a)

def varargs(*args):
    return args

print(varargs(1, 2, 3))
