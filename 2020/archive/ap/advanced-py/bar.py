from math import sin,cos

def rectangular(r, theta):
    x = r*cos(theta)
    y = r*sin(theta)
    return x, y

print(rectangular(3, 2))
