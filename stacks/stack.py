class stack():
    def __init__(self):
        self.stack = [None]*0

    def push(self, element):
        self.stack.append(element)

    def pop(self):
        if self.is_empty():
            raise Exception("Stack is empty")
        return (self.stack.pop(len(self.stack)-1))

    def peek(self):
        if self.is_empty():
            raise Exception("Stack is empty")
        return self.stack[-1]

    def isEmpty(self):
        return len(self.stack) == 0
