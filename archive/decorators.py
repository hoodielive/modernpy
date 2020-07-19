def deco(orig_f):
    print('decorating: ', orig_f)
    return orig_f


@deco
def func():
    print('in func')

