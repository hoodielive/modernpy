# Stack
#
# A stack is a data structure that has push() and pop() operations.
# push() puts a new item onto the stack.  The pop() operation removes
# and returns the most recent item pushed.

def make_stack():
    pass

def push(s, item):
    pass

def pop(s):
    pass

s = make_stack()
push(s, 2)
push(s, 4)
push(s, 5)

assert pop(s) == 5
assert pop(s) == 4
assert pop(s) == 2
