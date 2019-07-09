# Search Trees.   Trees can also be represented by pairs.
#
# Members of a tree are nodes.  A node can be a tuple of the form
# 
#     (element, (left, right))
#
# When adding a new item, you follow the left path if the new
# item is <= element.  Otherwise, follow the right path.

def make_tree(element, left, right):
    return (element, (left, right))

def element(tree):
    return tree[0]

def left(tree):
    return tree[1][0]

def right(tree):
    return tree[1][1]

def additem(tree, item):
    # Create a new tree with item added to it.
    if tree == None:
        return make_tree(item, None, None)
    if element(tree) == item:
        return tree
    if element < element(tree):
        return make_tree(element(tree), additem(left(tree), item), right(tree), item)
    else:
        return make_tree(element, tree, additem(right(tree), item), left(tree), item)

def contains(tree, item):
    # Check if a tree contains item or not
    if tree == None:
        return False
    if element(tree) == item:
        return True
    if item < element(tree):
        return contains(left(tree), item)
    else:
        return contains(right(tree), item)

items = [10, 7, 13, 2]
elements = None
for x in items:
    elements = additem(elements, x)

assert all(contains(elements, x) for x in items)
assert additem(elements, 2) == elements
assert contains(additem(elements, 4), 4) == True

# CHALLENGE: Search trees could be used to represent sets.
# Can you implement the intersection and union operations?

def intersection(tree1, tree2):
    pass

def union(tree1, tree2):
    pass

def test_sets():
    a_items = [10, 7, 13, 2]
    b_items = [3, 7, 2, 16]

    a_tree = None
    for x in a_items:
        a_tree = additem(a_tree, x)

    b_tree = None
    for x in b_items:
        b_tree = additem(b_tree, x)

    c = intersection(a_tree, b_tree)
    assert all(contains(c, x) for x in [2, 7])
    assert all (not contains(c, x) for x in [3, 10, 13, 16])

    d = union(a_tree, b_tree)
    assert all(contains(d, x) for x in a_items + b_items)

# Uncomment to test sets
# test_sets()



