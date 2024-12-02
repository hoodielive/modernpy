def create_adder(x):
    def adder(y):
        return x + y
    return adder

add_10 = create_adder(10)
print(add_10(3))

# Closures in nested functions:
# We can use the nonlocal keyword to work with variables in nested scope
# which shouldn't be declared in the inner functions.

def create_avg():
    total = 0
    count = 0

    def avg(n):
        nonlocal total, count
        total += n
        count += 1
        return total / count
    return avg

avg = create_avg()
print(avg(5))

print((lambda x: x > 2)(3))

print(list(map(add_10, [1, 2, 3])))

print(list(map(max, [1, 2, 3], [4, 2, 1])))

print(list(filter(lambda x: x > 5, [3, 4, 5, 6, 7])))
