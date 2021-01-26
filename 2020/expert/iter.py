i = iter('abc')
print(next(i))
print(next(i))
print(next(i))

class CountDown:
    def __init__(self, step):
        self.step = step

    def __next__(self):
        """Return the next element."""
        if self.step <= 0:
            raise StopIteration
        self.step -= 1
        return self.step

    def __iter__(self):
        return self


count_down = CountDown(4)

for element in count_down:
    print(element)
else:
    print("end")


