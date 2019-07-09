# heap_9.py
#
# A heap is a tree structure where each element the tree
# is strictly less than any of the elements that appear 
# below it.    For example:
#
#               4
#              / \
#             7   11
#            /\   / \
#           9 15 13 20
#
# A heap is not the same as a search tree.   It's only
# requirement is that it maintain the so-called "heap condition"
# where each element is smaller than the value of any of its
# child elements.

def make_heap():
    # Make a new heap
    return ['heap', None]

def make_entry(value, left, right):
    return [value, [left, right]]

# get, set, get_left, get_right
def push_heap(heap, item):
    if heap[1] == None:
        heap[1] = make_entry(item, None, None)

def pop_heap(heap):
    # Remove the top item on the heap
    return heap.pop(item)

# Application: Show how a heap can be used to implement an
# event calendar.  The event calendar holds "events" and the
# time at which they take place.  Removing an item from the
# calendar always gives you the next event.   This is how
# you create a priority queue.




