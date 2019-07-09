# 1. Points and Lines
#
# A point is represented by a (x, y) coordinate pair. 
# A line-segment is represented by two points.  For
#
#    segment = ((x1, y1), (x2, y2))
#
# The midpoint of a line segment is the point:
#
#       ((x1+x2)/2,  (y1+y2)/2)
#
# Show how the midpoint would be calculated if a line
# segment were represented by a pair of tuples of
# the form ((x1, y1), (x2, y2)).

def midpoint(segment):
    pass

segment = ((1, 3), (4, 5))
mid = midpoint(segment)
assert mid == (2.5, 4)
