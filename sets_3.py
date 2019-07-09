# sets
#
# A set is a collection of unique items.   Assume that sets can be represented 
# in the same way as lists

elements = (1, (2, (3, None)))

def in_set(set, item):
    '''
    Return True if item is found in set
    '''
    pass

assert in_set(elements, 2) == True
assert in_set(elements, 4) == False

def add_item(set, x):
    '''
    Add a new item x to a set.  Does nothing
    if x is already part of the set
    '''
    pass

# assert add_item(elements, 3) == elements
# assert in_set(add_item(elements, 4), 4) == True

def intersection(set1, set2):
    '''
    Compute the set of all items that are in both set1 and set2
    '''
    pass

a = (1, (2, (3, None)))
b = (2, (3, (4, None)))
c = intersection(a, b)
# assert all(in_set(c, x) for x in [2, 3])

def union(set1, set2):
    '''
    Compute the set of all items that are in either set1 or set2.
    '''
    pass

d = union(a, b)
# assert all(in_set(d, x) for x in [1,2,3,4])

