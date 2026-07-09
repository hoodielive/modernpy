class Point: 
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def where_is(point):
        match point: 
            case Point(x=0,y=0):
                print("Origin")
            case Point(x=0, y=y):
                print(f"Y={y}")
            case Point(x=x, y=0):
                print(f"X={x}")
            case Point():
                print("Somewhere else.")
            case _:
                print("Not a point.")


def f(ham: str, eggs: str = 'eggs') -> str:
    print("Annotations: ", f.__annotations__)
    print("Arguments:", ham, eggs)
    return ham + ' and ' + eggs

f('spam')


def standard_arg(arg):
    print(arg)

def pos_only_arg(arg, /):
    print(arg)

def kwd_only_arg(*, arg):
    print(arg)

def combined_example(pos_only, /, standard, *, kwd_only):
    print(pos_only, standard, kwd_only)

standard_arg(2)
standard_arg(arg=2)
