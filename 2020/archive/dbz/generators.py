nums = [1,2,3,4]

squares = (x * x for x in nums)

print(squares)


for n in squares:
    print(n, end=' ')

def sumsquares(nums):
    squares = (x * x for x in nums)
    total = sum(squares)
    return total

sumsquares(nums)

items = filenames = []

print(','.join(str(x) for x in items))

if any(name.endswith('.py') for name in filenames):
    ...


import sys
a = '\x00'
print(sys.getsizeof(a))
