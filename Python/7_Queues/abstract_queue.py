class AbstractQueue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, item): # or append
        self.items.append(item)

    def dequeue(self): # or pop
        if self.is_empty():
            raise IndexError("Dequeue from empty queue")
        return self.items.pop()

    def size(self):
        return len(self.items)

    def peek(self):
        if self.is_empty():
            raise IndexError("Peek from empty queue")
        return self.items[0]
    
    