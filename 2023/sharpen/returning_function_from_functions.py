def parent(num):
    def first_child():
        return "Hi, I am Oyeku."

    def second_child():
        return "Call me O ye ye iku."

    if num == 1:
        return first_child
    else:
        return second_child

first = parent(1)
second = parent(2)

print(first())
print(parent(1)())
print(parent(2)())
print(second())
