"""
File: arrayqueue.py
Project 8.2
"""

from arrays import Array
from abstract_collection import AbstractCollection

class ArrayQueue(AbstractCollection):
    """An array-based queue implementation."""

    # Simulates a circlular queue within an array

    # Class variable
    DEFAULT_CAPACITY = 10

    # Constructor
    def __init__(self, source_collection = None):
        """Sets the initial state of self, which includes the
        contents of sourceCollection, if it's present."""
        self.front = self.rear = -1
        self.items = Array(ArrayQueue.DEFAULT_CAPACITY)
        AbstractCollection.__init__(self, source_collection)

    # Accessor methods
    def __iter__(self):
        """Supports iteration over a view of self."""
        cursor = self.front
        while cursor != self.rear:
            yield self.items[cursor]
            if cursor == len(self.items) - 1:
                cursor = 0
            else:
                cursor += 1
        if cursor == self.rear and cursor != -1:
            yield self.items[cursor]
    
    def peek(self):
        """Returns the item at the front of the queue.
        Precondition: the queue is not empty.
        Raises: KeyError if queue is empty."""
        if self.isEmpty():
            raise KeyError("Queue is empty")
        return self.items[self.front]

    # Mutator methods
    def clear(self):
        """Makes self become empty."""
        self.front = self.rear = -1
        self.size = 0
    
    def add(self, item):
        """Inserts item at rear of the queue."""
        if len(self) == len(self.items):
            temp_array = Array(len(self)*2)
            cursor = 0
            for i in self:
                temp_array[cursor] = i
                cursor += 1
            self.items = temp_array
            self.front = 0
            self.rear = cursor - 1
        
        if self.is_empty():
            self.front = 0
            self.rear  = 0
        else:
            self.rear = (self.rear + 1) % len(self.items)

        self.items[self.rear] = item
        self.size += 1
    
    def pop(self):
        """Removes and returns the item at the front of the queue.
        Precondition: the queue is not empty.
        Raises: KeyError if queue is empty.
        Postcondition: the front item is removed from the queue."""
        if len(self) == 0:
            raise KeyError("Queue is empty")

        rv = self.items[self.front]

        if self.size == 1:
            self.front = self.rear = -1
        else:
            self.front = (self.front + 1) % len(self.items)    
        self.size -= 1


        return rv

         