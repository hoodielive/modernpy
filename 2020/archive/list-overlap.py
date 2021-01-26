a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

def func(one, two):
    return one & two


print(func(set(a), set(b)))

#set_theory = { s for s in a and b }

# print(set_theory)
returned_list = [func(x,y) for x in a for y in b if x in a and y in b]

# print(returned_list)
# print(set(a) & set(b))