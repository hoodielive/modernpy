str1 = "0123456789"

for i in range(10):
    print(str1[i], " and ")

def remove_dupes(seq):
    seen = set()
    items = []
    for item in seq:
        if item not in seen:
            seen.add(item)
            items.append(item)
    return items

content = "0123499999433382884939599929393948483848483"

print(remove_dupes(content))
