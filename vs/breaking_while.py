count = 0
while count < 5:
    print('.', end='')
    count += 1
    if count > 3:
        break
else:
    print()
    print("Oh, else the loop")
