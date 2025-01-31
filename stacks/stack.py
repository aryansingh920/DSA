class stack():
    def __init__(self, length):
        self.stack = [None]*length

    def push(self, element):
        self.stack.append(element)

    def pop(self):
        self.stack.pop()

    def peek(self):
        return self.stack[-1]

    def isEmpty(self):
        return len(self.stack) == 0


    
