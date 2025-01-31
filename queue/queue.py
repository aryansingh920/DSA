class Queue():
    def __init__(self):
        self.queue = [None]

    def enqueue(self, element):
        self.queue.append(element)

    def dequeue(self):
        if self.isEmpty():
            raise Exception("Queue is empty")
        return self.queue.pop(0)

    def peek(self):
        if self.isEmpty():
            raise Exception("Queue is empty")
        return self.queue[0]

    def isEmpty(self):
        return len(self.queue) == 0
