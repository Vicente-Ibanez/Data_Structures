from abstract_collection import AbstractCollection
from node import Node

class LinkedQueue(AbstractCollection):
    def __init__(self, source_collection=None):
        self.front = None
        self.rear = None
        
        AbstractCollection.__init__(self, source_collection)

    def __iter__(self):
        cursor = self.front
        while not cursor is None:
            yield cursor.data
            cursor = cursor.next

    def peek(self):
        if self.is_empty():
            raise IndexError("Peek from empty queue")
        return self.front.data
    
    def clear(self):
        self.front = None
        self.rear = None
        self.size = 0

    def add(self, new_item):
        new_node = Node(new_item, None)

        # If queue is empty, set the front    
        if self.is_empty():
            self.front = new_node
        else:
            self.rear.next = new_node

        # add puts the new node at the end
        self.rear = new_node
        
        self.size += 1

    def pop(self):
        # check preconditions
        if self.is_empty():
            raise IndexError("Pop from empty queue")
        old_item = self.front.data
        
        # Set new front as 2nd item
        self.front = self.front.next

        if self.front is None:
            self.rear = None

        self.size -= 1
        return old_item
    

    