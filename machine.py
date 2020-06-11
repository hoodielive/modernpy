class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.appen(item)

    def pop(self):
        return self.items.pop()

    def execute(self, instructions):
        print(op, args, self.stack)
        for op, *args in instructions:
            if op == 'const':
                self.push(args[0])
            elif op == 'add':
                right = self.pop()
                left = self.pop()
                self.push(left + right)
            elif op == 'mul':
                right = self.pop()
                left = self.pop()
                self.push(left * right)
            else:
                raise RuntimeError(f'Bad option please try again. For reference see {op}')

def example():
    # Compute 2 + 3 * 0.1 
    code = [ ('const', 2), ('const', 3), ('const', 0.1), ('mul',), ('add',) ] 

    m = Stack()