def TRUE(a):
    return lambda b: a()   # Call a to evaluate it

def FALSE(a):
    return lambda b: b()    # Call b to evaluate it (hack)


def PAIR(a):
    return lambda b:  lambda z: z(lambda: a)(lambda: b)   # Patch
	
	
def FACTORIAL(n):
    return ISZERO(n)(lambda: ONE)(lambda: MUL(n)(FACTORIAL(PRED(n))))

