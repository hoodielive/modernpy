def add(x, y):
    print("x is {} and y is {}".format(x, y))
    return x + y # Returns with a return statement

add(5, 6)

add(y=6, x=5)

def varargs(*args):
    return args

varargs(1, 2, 3)

def keyword_args(**kwargs):
    return kwargs

keyword_args(big="foot", loch="ness")

def all_the_args(*args, **kwargs):
    print(args)
    print(kwargs)

args = (1, 2, 3, 4)
kwargs = { "a": 3, "b": 4 }

all_the_args(*args)
all_the_args(**kwargs)
all_the_args(*args, **kwargs)

def swap(x, y):
    return x, y

x = 1
y = 2
x, y = swap(x, y)

x = 5

def set_x(num):
    x = num
    print(x)

def set_global_x(num):
    global x
    print(x)
    x = num
    print(x)

set_x(43)
set_global_x(6)

# Python has first class functions.
def create_adder(x):
    def adder(y):
        return x + y
    return adder

add_10 = create_adder(10)
add_10(3)

print((lambda x: x > 2)(3))
print((lambda x, y: x ** 2 + y ** 2)(2, 1))
print(list(map(add_10, [1,2,3])))
print(list(map(max, [1, 2, 3], [4, 2, 1])))


print(list(filter(lambda x: x > 5, [3, 4, 5, 6, 7])))

x = [add_10(i) for i in [1, 2, 3]]
y = [x for x in [3, 4, 5, 6, 7] if x > 5]
print(x)
print(y)


