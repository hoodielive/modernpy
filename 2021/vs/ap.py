class Person:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"Person({self.name})"

    def __mult__(self, p):
        if type(x) is not int:
            raise Exception("Invalid argument, must be int.")
        self.name = self.name * x

    def __call__(self, y):
        print(y)


p = Person("Larry")
print(p)