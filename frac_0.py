# 0. Fractions.
#
# A fraction consists of a numerator/denominator.  
#
#        numerator
#       -----------
#       denominator
#
# To add two fractions, they need to have a common denominator.  Here is
# the calculation:
#
#     a   c      a*d + c*b
#     - + -   =  ---------
#     b   d        b * d
#
# To multiply fractions, you multiply numerator/denominator separately
#
#     a   c      a * c
#     - * -  =   -----
#     b   d      b * d
#
#
# Suppose you represent fractions as a tuple (numer, denom).  Write
# the following functions that perform arithmetic:

def add_fraction(x, y):
    pass

a = (2, 3)
b = (4, 5)

assert add_fraction(a, b) == (22, 15)

def mul_fraction(x, y):
    pass

# assert mul_fraction(a, b) == (8, 15)
