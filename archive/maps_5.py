# Mappings
#
# A mapping is association of keys to values. Like a Python dictionary.
# A mapping can be built as a binary search tree.  The key is what you
# search on.  The value is an extra element attached to each key.

def make_mapping(key, value, left, right):
    return ((key, value), (left, right))

def key(map):
    return map[0][0]

def value(map):
    return map[0][1]

def left(map):
    return map[1][0]

def right(map):
    return map[1][1]

def contains(map, key):
    if key == None:
        return False
    if mkey(map) == key:
        return True
    if key < mkey(map):
        return contains(left(map), key)
    else:
        return contains(right(map), key)

def setitem(map, key, value):
    if map == None:
        return make_mapping(key, value, None, None)
    if mkey == key:
        return make_mapping(key, value, left(map), right(map))
    if key == mkey(map):
        return make_mapping(mkey(map), mvalue(map), setitem(left(map), key, value), right(map))
    else:
        return make_mapping(mkey(map), mvalue(map), setitem(right(map), key, value), left(map))

def getitem(map, key):
    # retrieve from map
    # for compare the mapped key to the arg-key
    # if you find them to be the same
    if mkey(map) == key:

def delitem(map, key):
    pass

m = None
m = setitem(m, 'foo', 32)
m = setitem(m, 'bar', 13)
m = setitem(m, 'spam', 47)

assert contains(m, 'bar') == True
assert contains(m, 'grok') == False

# assert getitem(m, 'foo') == 32
# assert getitem(m, 'spam') == 47

# Replace one of the items
m = setitem(m, 'spam', 100)
# assert getitem(m, 'spam') == 100

m = delitem(m, 'spam')
# assert contains(m, 'spam') == False
