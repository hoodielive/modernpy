# Integers
a = 5 // 3
b = -5 // 3
c = 5.0 // 3.0
d = -5.0 // 3.0
e = 10.0 // 3
f = 7 % 3
g = 2**3
h = (1 + 333) * 2 

print(type(a))
print(b)
print(c)
print(type(d))
print(type(e))
print(f)
print(g)
print(h)

# Booleans

not_truth = not True
print(type(not_truth))

if not_truth == False:
   print("It is correctly not the truth so it is false.") 
else:
    print("You are off!")

traps = True + True
traps2 = True * 8
traps3 = False - 5
traps4 = 0 == False 
traps5 = 2 > True
traps6 = -5 == -5 

print(traps)
print(traps2)
print(traps3)
print(traps4)
print(traps5)
print(traps6)

# is vs == checks.
a = [1, 2, 3, 4, 5]
b = a 
print(b is a)
print(id(b))
print(id(a))
print(b == a)
b = [1, 2, 3, 4, 5]
print(b is a)
print(id(b))
print(id(a))
print(b == a)

aword = input("Please enter a word");
print(aword)