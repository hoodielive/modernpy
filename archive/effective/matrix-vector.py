matrix = [[ 1,2,3], [4,5,6], [7,8,9]] 

flat = [x for row in matrix for x in row]

print(flat)

# A matrix is a list within a list. Struct within a struct.
squared = [[x**2 for x in row] for row in matrix] 
print(squared)

# List/Sublist.
flat = [x for sublist1 in matrix
        for sublist2 in sublist1
        for x in sublist2]

print(flat)
