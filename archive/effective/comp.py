a = [1,2,3,4,5,6,7,8,9,10] 

# the long way
squares = map(lambda x: x**2, a)

# the short way
squares = [x**2 for x in a ] 

print(squares) 

# Print even squares.
# Works but is a lot going on.
alt = map(lambda x: x**2, filter(lambda x: x % 2 == 0, a)) 
print(list(alt))

# You can do this with just comprehensions.
xcomp = [x**2 for x in a if x % 2 == 0] 
assert xcomp == list(xcomp)
print(xcomp) 
