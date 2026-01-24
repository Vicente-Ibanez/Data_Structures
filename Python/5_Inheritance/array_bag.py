from .arrays import Array
from abstract_bag import AbstractBag

class ArrayBag(AbstractBag):
    """An array-based bag implementation."""

    # Class Variable
    DEFAULT_CAPACITY = 10

    # Constructor
    def __init__(self, source_collection=None):
        """Sets the initial state of self, which includes
        the contents of source_collection, if it's present."""
        self.items = Array(ArrayBag.DEFAULT_CAPACITY)
        AbstractBag.__init__(self, source_collection)

    def __iter__(self):
        """Supports iteration over a view of self"""
        cursor = 0
        while cursor < len(self):
            yield self.items[cursor]
            cursor += 1

    def __add__(self, other):
        """Returns a new bag containing the contents of self and other"""
        result = ArrayBag(self)
        for item in other:
            result.add(item)
        return result
    
    # Mutator methods
    def clear(self):
        """Makes self become empty"""
        self.size = 0
        self.items = Array(ArrayBag.DEFAULT_CAPACITY)        

    def add(self, item):
        """Adds item to self"""
        if len(self) == len(self.items):
            self.items = self.items.resize(2 * len(self.items))

        self.items[len(self)] = item
        self.size += 1

    def remove(self, item):
        """Precondition: item is in self
        Raises: KeyError if item is not in self
        Postcondition: item is removed from self"""
        
        # 1. check precon and raise an exception if necessary
        if not item in self:
            raise KeyError(str(item) + " not in bag")
        
        # 2. Search for index of target item
        target_index = 0
        for target_item in self:
            if target_item == item:
                break
            target_index += 1

        # 3. Shift items to the right of target left by one position
        for i in range(target_index, len(self) - 1):
            self.items[i] = self.items[i + 1]

        # 4. Decrement logical size
        self.size -= 1

        # 5. Check array memory here and decrease if necessary
        if 0 < len(self) <= len(self.items) // 4 and \
           len(self.items) // 2 >= ArrayBag.DEFAULT_CAPACITY:
            self.items = self.items.resize(len(self.items) // 2)