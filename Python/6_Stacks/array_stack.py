from arrays import Array
from abstract_stack import AbstractStack

class ArrayStack(AbstractStack):
    """ An array-based stack implementation """

    DEFAULT_CAPACITY = 10

    def __init__(self, source_collection=None):
        """ Sets the initial state of self, which includes
        the contents of source_collection, if it's present """
        self._items = Array(ArrayStack.DEFAULT_CAPACITY)
        AbstractStack.__init__(self, source_collection)

    # Accessor methods
    def __iter__(self):
        """ Supports iteration over a view of self.
         Visits items from bottom to top of stack """
        cursor = 0
        while cursor < len(self):
            yield self._items[cursor]
            cursor += 1

    def peek(self):
        """ Returns the item at the top of the stack.
        Precondition: the stack is not empty
         Raises KeyError if the stack is empty """
        if self.is_empty():
            raise KeyError("The stack is empty")
        return self._items[len(self) - 1]

    # Mutator methods
    def clear(self):
        """ Makes self become empty """
        self.size = 0
        self.items = Array(ArrayStack.DEFAULT_CAPACITY)

    def push(self, item):
        """ Inserts items at top of the stack """
        # Resize array here if necessary
        if len(self) == len(self.items):
            self.resize(2 * len(self.items))
        self.items[len(self)] = item
        self.size += 1

    def pop(self):
        """ Removes and returns the item at the top of the stack.
        Precondition: the stack is not empty
         Raises KeyError if the stack is empty """
        if self.is_empty():
            raise KeyError("The stack is empty")
        
        old_item = self.items[len(self) - 1]
        self.size -= 1
        # Resize array here if necessary
        if 0 < len(self) < len(self.items) // 4:
            self.resize(len(self.items) // 2)

        return old_item

    