op = '*'

if op == '+':
    r = add(x, y)
elif op == '-':
    r = sub(x, y)
elif op == '*':
    r = mul(x, y)
elif op == '/':
    r = div(x, y)

# or

ops = {
    '+' : add,
    '-' : sub,
    '*' : mul,
    '/' : div,
}

r = ops[op](x,y)

print(r)