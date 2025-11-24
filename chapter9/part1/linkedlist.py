"""
File: linkedlist.py
Project 9.1

Includes the list iterator for the LinkedList class.
"""

from node import TwoWayNode
from abstractlist import AbstractList

class LinkedList(AbstractList):
    """A link-based list implementation."""

    def __init__(self, sourceCollection = None):
        """Sets the initial state of self, which includes the
        contents of sourceCollection, if it's present."""
        # Uses a circular linked structure with a dummy header node
        self.head = TwoWayNode()
        self.head.previous = self.head.next = self.head
        AbstractList.__init__(self, sourceCollection)

    # Helper method returns node at position i
    def getNode(self, i):
        """Helper method: returns a pointer to the node at position i."""
        if i == len(self):
            return self.head
        elif i == len(self) - 1:
            return self.head.previous
        probe = self.head.next
        while i > 0:
            probe = probe.next
            i -= 1
        return probe

    #Accessor methods
    def __iter__(self):
        """Supports iteration over a view of self."""
        cursor = self.head.next
        while cursor != self.head:
            yield cursor.data
            cursor = cursor.next

    def __getitem__(self, i):
        """Precondition: 0 <= i < len(self)
        Returns the item at position i.
        Raises: IndexError."""
        if i < 0 or i >= len(self):
            raise IndexError("List index out of range")
        return self.getNode(i).data

    # Mutator methods
    def clear(self):
        """Makes self become empty."""
        self.size = 0
        self.modCount = 0
        self.head = TwoWayNode()
        self.head.previous = self.head.next = self.head
        
    def __setitem__(self, i, item):
        """Precondition: 0 <= i < len(self)
        Replaces the item at position i.
        Raises: IndexError."""
        if i < 0 or i >= len(self):
            raise IndexError("List index out of range")
        self.getNode(i).data = item

    def insert(self, i, item):
        """Inserts the item at position i."""
        if i < 0: i = 0
        elif i > len(self): i = len(self)
        theNode = self.getNode(i)
        newNode = TwoWayNode(item, theNode.previous, theNode)
        theNode.previous.next = newNode
        theNode.previous = newNode
        self.size += 1
        self.incModCount()

    def pop(self, i = None):
        """Precondition: 0 <= i < len(self).
        Removes and returns the item at position i.
        If i is None, i is given a default of len(self) - 1.
        Raises: IndexError."""
        if i == None: i = len(self) - 1
        if i < 0 or i >= len(self):
            raise IndexError("List index out of range")
        theNode = self.getNode(i)
        item = theNode.data
        theNode.previous.next = theNode.next
        theNode.next.previous = theNode.previous
        self.size -= 1
        self.incModCount()
        return item

    def listIterator(self):
        """Returns a list iterator."""
        return LinkedList.ListIterator(self)

    class ListIterator(object):
        """Represents the list iterator for linked list."""

        def __init__(self, backingStore):
            self.backingStore = backingStore
            self.cursor = None # current node
            self.index = -1 # cursor position
            self.mostRecent = None
            # self.modCount = backingStore.modCount
            # raise Exception("List iterator not implemented yet.")

        def first(self):
            self.cursor = self.backingStore.head.next
            self.index = 0
            self.mostRecent = None
        
        def last(self):
            self.cursor = self.backingStore.head.previous
            self.index = len(self.backingStore) - 1
            self.mostRecent = None

        def hasNext(self):
            """returns True if the iterator has a next item or False otherwise."""
            if self.cursor == None: # cursor not defined
                return False

            return self.cursor != self.backingStore.head # prevents looping back around
        
        def next(self):
            """returns the current item and advances the cursor to the next item"""
            if not self.hasNext():
                raise KeyError("No next value")
            self.mostRecent = self.cursor
            self.cursor = self.cursor.next
            self.index += 1
            return self.mostRecent.data
        
        def hasPrevious(self):
            """returns True if the iterator has a previous item or False otherwise"""
            if self.cursor == None:
                return False
            return self.cursor.previous != self.backingStore.head
        
        def previous(self):
            if not self.hasPrevious():
                raise KeyError("No previous value")
            self.cursor = self.cursor.previous
            self.mostRecent = self.cursor
            self.index -= 1
            return self.mostRecent.data
        
        def replace(self, item):
            """ replaces the items at the current position with item."""
            if self.mostRecent == None:
                raise KeyError("Cursor is None")
            self.mostRecent.data = item

        def insert(self, item):
            """adds item to the end if the current position is undefined, or inserts it at that position."""
            if self.mostRecent == None: # insert at end
                self.backingStore.insert(len(self.backingStore), item)
            else: # insert new node
                if self.cursor == self.mostRecent: # last call was next()
                    self.backingStore.insert(self.index, item)
                else: # last call was previous
                    self.backingStore.insert(self.index-1, item)
                self.index += 1 # inserted node, so move cursor to adjust for new node
                self.mostRecent = None

        def remove(self):
            if self.mostRecent == None:
                raise KeyError("Cursor is None")
            if self.cursor == self.mostRecent: # Means last call was next()
                self.cursor = self.cursor.next
                self.backingStore.pop(self.index)
            else: # Last call was previous()
                self.backingStore.pop(self.index - 1)
                self.index -= 1

            self.mostRecent = None

            if len(self.backingStore) == 0: # If list is empty, reset variables
                self.cursor = None
                self.index = -1

