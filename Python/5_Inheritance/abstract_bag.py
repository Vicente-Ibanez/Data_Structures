
class AbstractBag(object):
    """An array-based bag implementation."""

    # Class Variable
    DEFAULT_CAPACITY = 10

    # Constructor
    def __init__(self, source_collection=None):
        """Sets the initial state of self, which includes
        the contents of source_collection, if it's present."""
        self.size = 0
        if source_collection:
            for item in source_collection:
                self.add(item)

    # Accessor methods
    def is_empty(self):
        """Returns True if len(self) == 0"""
        return self.size == 0
    
    def __len__(self):
        """Returns number of items in self"""
        return self.size
    
    def __str__(self):
        """Returns a string representation of self"""
        return "{" + ", ".join(map(str, self)) + "}"
    
    def __add__(self, other):
        """Returns a new bag containing the contents of self and other"""
        result = type(self)(self)
        for item in other:
            result.add(item)
        return result
    
    def __eq__(self, other):
        """Returns True if self equals other"""
        if self is other: return True

        if type(self) != type(other) or \
            len(self) != len(other):
            return False
       
        otherIter = iter(other)
        for item in self:
            if item != next(otherIter):
                return False
        return True    

    def count(self, item):
        """Returns the number of instances of item in self."""
        total = 0
        for nextItem in self:
            if nextItem == item:
                total += 1
        return total

    def add(self, item):
        pass
