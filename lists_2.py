# 1. Linked lists.

data = (1, (2, (3, None)))

# Implement the following functions.  All of these functions take a
# linked list as input and return a new linked list as output.  The
# original list is NOT modified.  You are *ONLY* allowed to use
# 2-tuples to solve the problem.  No other Python data structures
# (lists, sets, dicts, etc.)  may be used.

def length(items):
    '''
    Return the number of elements in items
    '''
    count = 0 
    while items:
        count += 1 
        items = items[l]
    return count
assert length(data) == 3

def length(items):
    if items:
        return 1 + length(items[1])
    else: 
        return 0
def getitem(items, n):
    '''
    Return the nth item
    '''
    count = 0 
    while n > 0:
        items = items[1]
        n -= 1 
    return items[0] 
# assert getitem(data, 1) == 2
    
def append(items, item):
    '''
    Add a new item to the end of the list. Note:
    this returns a new list.
    '''
    # My feeble attempt
    #item = [] 
    #x = tuple(x for x in items)
    #item.append((x)) 
    #item.append(item)
    #return tuple(item)

    # Dave's Implementation
    lastitem = (item, None)
    nitems = length(items) 
    while nitems > 0: 
        lastitem = (getitem(items, nitems -1), lastitem)
        nitems -= 1 
    return lastitem
     

# assert append(data, 4) == (1, (2, (3, (4, None))))

def extend(items, more):
    '''
    Attach the items in list "more" to items.  This
    returns a new list.
    '''
    pass

# assert extend(data, (4, (5, None))) == (1, (2, (3, (4, (5, None)))))

def remove(items, index):
    '''
    Remove the item at a given index. Returns a new list.
    '''
    nitems = length(items)
    item_to_pluck = (getitem(items[index]))
    lastitem = (getitem(items, nitems -1), lastitem)
    while nitems > 0: 
        


# assert remove(data, 1) == (1, (3, None))

def reverse(items):
    '''
    Create a list with items in reverse order
    '''
    

# assert reverse(data) == (3, (2, (1, None)))

def map(func, items):
    '''
    Apply the function func to each item in items.
    '''
    if items:
        return (func(items[0]), map(func, items[1]))
    else: 
        return None

# assert map(lambda x: x*x, data) == (1, (4, (9, None)))

def filter(func, items):
    '''
    Return a new list consisting only of the items where func(item) is True
    '''

# assert filter(lambda x: x > 2, data) == (3, None)
