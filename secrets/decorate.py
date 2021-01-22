def first_func(val):
    return print(val)


new_name = first_func

first_func("Spam!")
print(new_name("Spam too!"))

# Functions can be used as arguments for other functions.
# Some Python built-in functions, such as map/filter use
# this feature to do their jobs.


def mult(x, y):
    return x * y


def div(x, y):
    return x / y


def math(func, x, y):
    result = func(x, y)
    return result


math(mult, 4, 2)


math(div, 4, 2)
