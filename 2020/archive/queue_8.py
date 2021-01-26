# Queues.py
#
# A queue is a data structure that stores items in order like
# a list, but items can be pushed on the end and popped off the front.

def make_queue():
    return [None, None] # [Head, Tail]

def is_empty(q):
    return q[0] == None

def put(q, item):
    node = [item, None]
    if is_empty(q):
        q[0] = None
        q[1] = None
    else:
        q[1][1] = node
        q[1] = node

def get(q):
    node = q[0]
    q[0] = node[1]
    return node[0]

q = make_queue()
put(q, 13)
put(q, 20)
put(q, 99)

assert get(q) == 13
assert get(q) == 20
assert get(q) == 99


