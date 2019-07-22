def mul(a, b):
    # Implement multiply only using add/sub/other bit operations 
    result = 0 
    while b > 0:
        if b & 1:
            result += a
            b -= 1
        else:
            a = a << 1 # a * 2
            b = b >> 1 # b / 2
    return result 
print(mul(2, 1000000))

# 3. Compute Square Root
def sqrt(x):
    guess = 1
    while (abs(guess * guess - x) > 0.00000001):
            guess = (guess + x/guess) / 2
    return guess
print(sqrt(2))

# the sum of n integers (infinite)
