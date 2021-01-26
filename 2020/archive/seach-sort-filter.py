import bisect
import timeit

values = [ 5, 3, 1, 7 ]
sorted_value = sorted(values)

def bisect_search(container, value):
    index = bisect.bisect_left(container, value)
    return index < len(container) and container[index] == value

#bisect.bisect_left(values, 4)
print(bisect_search(sorted_value, 7))