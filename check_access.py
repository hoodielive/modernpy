xcaps = ['l', 'r', 'l', 'l', 'r', 'l', 'r']

intervals = []

def check_access(caps):
    start = forward = backward = 0
    for x in range(1, len(caps)):
        if caps[start] != caps[1]:
            intervals.append((start, x - 1, caps[start]))
        if caps[start] == '1':
            forward += 1
        else:
            backward += 1
        start = x


check_access(xcaps)