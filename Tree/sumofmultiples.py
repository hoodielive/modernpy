# if we list all the natural numbers below 10 that are multiples of 3 or 5, we get
# 3, 5, 6, and 9. The sume of these multiples is 23. Find the sum of all the multiples
# of 3 or 5 below 100.

def f(x):
    return print(x % 3 == 0 or x % 5 == 0)
    #print(sum(filter(f, range(1, 1000))))

f(1000)
