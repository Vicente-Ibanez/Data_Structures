"""
Stack, AKA push-down stack.

Ordered collection of items. 
* New items and removal of items takes place at the same end (the top).
* The bottom/front is known as the base.
* LIFO: last in, first out

"""
class Stacks():
    def __init__(self):
        self.items = []
    
    def is_empty(self):
        return self.items == []

    def push(self, item): # O(1) 
        self.items.append(item)

    def pop(self): # 0(1)
        return self.items.pop()

    def peek(self): # 0(1)
        return self.items[-1]

    def size(self): # 0(1)
        return len(self.items)
    