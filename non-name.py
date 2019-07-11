#!/usr/bin/env python

def fact(n):
    return 1 if n == 0 else n * fact(n-1)

fact(3)

(lambda r: lambda n: 1 if n == 0 else n * r(r)(n - 1))(lambda r: lambda n: 1 if n == 0 else n * r(r)(n - 1))(5)
