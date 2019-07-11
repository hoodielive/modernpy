f = lambda x: 3 * x + 1 

print(f(2))   # replace x with 2 

print(f(2+3))

# No packages/modules
# No objects 
# No numbers 
# No strings 
# No DataTypes 

# What if you only had functions ? 

def f(x):
    return x + 1    # No. No numbers No +

def f(x, y):
    ... # No. Single arg only. 

def f(x):
    return x  # Yes.

def f(x):
    return x(x) # Yes.  x is a function. 

def f(x):
    def g(y):
        return x(y)
    return g

# Model a switch
def LEFT(a):
    def f(b):
        return a 
    return f

def RIGHT(a):
    def f(b):
        return b
    return f

LEFT('5v')('gnd')
RIGHT('5v')('gnd')
LEFT('loud')('soft')
RIGHT('loud')('soft')

def add(x,y):
    return x + y

def add(x): # Currying. Take multiple args and turn them into single functions.
    def f(y):
        return x + y
    return f

def TRUE(x):
    return lambda y: x

def FALSE(x):
    return lambda y: y

TRUE('5v')('gnd')
FALSE('5v')('gnd')

TRUE(TRUE)(FALSE)
f = lambda x: x
TRUE(f)(FALSE)

# How would you do NOT? 
def NOT(x):
    return x(FALSE)(TRUE)

assert NOT(TRUE) is FALSE
assert NOT(FALSE) is TRUE

NOT(TRUE)
NOT(FALSE)

# What about AND and OR 
def AND(x):
    return lambda y: x(y)(x)

assert AND(TRUE)(TRUE)
assert AND(TRUE)(FALSE)
assert AND(FALSE)(TRUE)
assert AND(FALSE)(FALSE)

def OR(x):
    return lambda y: x(x)(y)

assert OR(TRUE)(TRUE)
assert OR(TRUE)(FALSE)
assert OR(FALSE)(TRUE)
assert OR(FALSE)(FALSE)

ZERO =
ONE = lambda f: lambda x: f(x)
TWO = lambda f: lambda x: f(f(x))
THREE = lambda f: lambda x: f(f(f(x)))
FOUR = lambda f: lambda x: f(f(f(f(x))))

def incr(x):
    return x + 1 # Illegal.

# just for shits and giggles and shit.
incr(0)
incr(incr(0)) 
incr(incr(incr(0)))

def p(t):
    return (t[0]+1, t[0])

p((0,0)) 
THREE(p)((0,0))

a = FOUR(THREE)
a(incr)(0)
