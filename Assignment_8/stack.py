class Stack:
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            None

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        else:
            None

    def is_empty(self):
        return len(self.stack) == 0


s = Stack()
s.push(1)
s.push(2)
print(s.peek())
print(s.pop())
print(s.is_empty())
