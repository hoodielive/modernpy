list_of_music = {
    'musiq soulchild': 156,
    'summer walker': 141,
    'H.E.R': 135,
    'Daniel Caesar': 240,
    'Sebastian Michaels': 109
}

print(sum(list_of_music.values()))

v = { key:value for key, value in list_of_music.items() if value > 200 }

print(v)

def findSmallest(arr):
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index

print(findSmallest([5,3,4,100,1,99,83,2]))


def selectionSort(arr):
    new_arr = []
    for i in range(len(arr)):
        smallest = findSmallest(arr)
        new_arr.append(arr.pop(smallest))
    return new_arr

print(selectionSort([5,3,6,2,10]))