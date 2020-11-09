from collections import OrderedDict

def fun(**kwargs):
    print(kwargs)

fun(a=1, b=2, c=3)

print(OrderedDict((str(number), None) for number in range(5)).keys())



