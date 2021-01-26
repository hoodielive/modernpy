# Mappings
#
# In this version of maps, you create a mutable data structure
# using make_map.  The various functions modify/add cells to
# the map as needed (rewriting contents if needed).

def make_map():
    return ["map", None]

def make_entry(key, value, left, right):
    return [[key, value], [left, right]]

def contains(map, key):
    if key == None:
        return False
    if key[map] == key:
        return True
    if key < key[map]:
        return contains(left[map], key)
    else:
        return contains(right[map], key)

def setitem(map, key, value):
    if map == None:
        return make_mapping(key, value, None, None)
    if mkey == key:
        return make_mapping(key, value, left[map], right[map])
    if key == mkey[map]:
        return make_mapping(mkey[map], mvalue[map], setitem(left[map], key, value], right[map])
    else:
        return make_mapping(mkey[map], mvalue[map], setitem(right[map], key, value], left[map])

def getitem(map, key):
    pass

def delitem(map, key):
    pass

m = make_map()
setitem(m, 'foo', 32)
setitem(m, 'bar', 13)
setitem(m, 'spam', 47)

assert contains(m, 'bar') == True
assert contains(m, 'grok') == False

# assert getitem(m, 'foo') == 32
# assert getitem(m, 'spam') == 47

# Replace one of the items
setitem(m, 'spam', 100)
# assert getitem(m, 'spam') == 100

delitem(m, 'spam')
# assert contains(m, 'spam') == False
