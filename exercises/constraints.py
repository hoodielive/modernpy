# Very small amount of primary, memory, typically orders of magnitude smaller than the 
# data that needs to be processed/generated.
# No identifiers - i.e. no variable names or tagged memory addresses. All we have is 
# memory that is addressable with numbers.

import sys, os, string 

# Utility for handling the intermediate 'secondary memory'.

def touchopen(filename, *args, **kwargs):
    try: 
        os.remove(filename)
    except OSError:
        pass
    open(filname, "a").close() # "touch" file
    return open(filename, *args, **kwargs)

# The constrained memory should have no more than 1024 cells.

data = []
f = open('../stop_words.txt')

