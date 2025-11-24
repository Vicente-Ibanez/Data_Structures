"""
File: arraysortedlist.py
Project 9.2

Completes the sorted list implementation.
"""

from arrays import Array
from abstractlist import AbstractList

class ArraySortedList(AbstractList):
    """An array-based sorted list implementation."""

    DEFAULT_CAPACITY = 10

    def __init__(self, sourceCollection = None):
        """Sets the initial state of self, which includes the
        contents of sourceCollection, if it's present."""
        self.items = Array(ArraySortedList.DEFAULT_CAPACITY)
        AbstractList.__init__(self, sourceCollection)

    def resize(self, array, logicalSize):
        """If the array needs resizing, resizes and returns
        the new array.  Otherwise, returns the olf array."""
        temp = None
        # If array is full
        if len(array) == logicalSize:
            temp = Array(2 * len(array))
        # If array is wasting space
        elif logicalSize < .25 * len(array) and \
             len(array) > ArraySortedList.DEFAULT_CAPACITY:
            temp = Array(round(.5 * len(array)))
        # None of the above
        else:
            return array
        # Copy items to new array
        for i in range(logicalSize):
            temp[i] = array[i]
        return temp

    # Accessor methods
    def __iter__(self):
        """Supports iteration over a view of self."""
        cursor = 0
        while cursor < len(self):
            yield self.items[cursor]
            cursor += 1

    def __getitem__(self, i):
        """Precondition: 0 <= i < len(self)
        Returns the item at position i.
        Raises: IndexError."""
        if i < 0 or i >= len(self):
            raise IndexError("List index out of range")
        return self.items[i]

    def __index__(self, item):
        """Precondition: item is in the list.
        Returns the position of item.
        Raises: ValueError if the item is not in the list."""
        for i in range(len(self)):
            if item == self.items[i]:
                return i
        raise ValueError(f"{item} not in list.")
    
    def index(self, item):
        """Precondition: item is in the list.
        Returns the position of item.
        Raises: ValueError if the item is not in the list."""
        for i in range(len(self)):
            if item == self.items[i]:
                return i
        raise ValueError(f"{item} not in list.")


    def __contains__(self, item):
        """Returns True if item is in the list,
        or False otherwise."""
        try:
            self.__index__(item)
            return True
        except Exception:
            return False    

    # Mutator methods
    def clear(self):
        """Makes self become empty."""
        self.size = 0
        self.modCount = 0
        self.items = Array(ArraySortedList.DEFAULT_CAPACITY)

    def pop(self, i = None):
        """Precondition: 0 <= i < len(self).
        Removes and returns the item at position i.
        If i is None, i is given a default of len(self) - 1.
        Raises: IndexError."""
        if i == None: i = len(self)
        if i < 0 or i >= len(self):
            raise IndexError("List index out of range")
        item = self.items[i]
        for j in range(i, len(self) - 1):
            self.items[j] = self.items[j + 1]
        self.size -= 1
        self.incModCount()
        self.items = self.resize(self.items, len(self))
        return item

    def add(self, item):
        """Adds item to self.

            Empty or last item, place at the end
            Search for first item >= new item
            Open a hole for new item
            Insert item and update size"""
        
        if self.isEmpty() or item >= self[len(self)-1]:
            self.items[len(self)] = item
            self.size += 1
            return
        
        for i in range(len(self.items)):
            if item <= self.items[i]:
                # Go backwards, start from the end
                for j in range(len(self), i, -1):
                    # for each index, copy the previous item
                    self.items[j] = self.items[j-1]
                self.items[i] = item
                break
            
        self.size += 1

        
        
    def listIterator(self):
        """Returns a list iterator."""
        raise Exception("List iterator for sorted lists not supported yet")

           


