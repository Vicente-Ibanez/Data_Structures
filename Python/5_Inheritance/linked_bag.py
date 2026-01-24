from .node import Node
from abstractbag import AbstractBag

class LinkedBag(AbstractBag):
    """A linked bag implementation."""

    # Constructor
    def __init__(self, source_collection=None):
        """Sets the initial state of self, which includes
        the contents of source_collection, if it's present."""
        self.items = None
        AbstractBag.__init__(self, source_collection)

    def __iter__(self):
        """Supports iteration over a view of self"""
        cursor = self.items
        while cursor != None:
            yield cursor.data
            cursor = cursor.next

    def add(self, item):
        """Adds item to self"""
        self.items = Node(item, self.items)
        self.size += 1

    def remove(self, item):
        """ Preco: item is in self
            Raises: KeyError if item is not in self
            Postcon: self does not contain item
        """
        # Check precondition and raise an exception if necesaary
        if not item in self:
            raise KeyError(str(item) + " not in bag")
        
        # Search for the node containing hte target item
        # probe will point to the target node, and trailer
        # will point to the node before it, if it exists
        probe = self.items
        trailer = None

        for target_item in self:
            if target_item == item:
                break
            trailer = probe
            probe = probe.next

        # Unhook the node to be deleted, either the first one o
        # or the one thereafter
        if probe == self.items:
            self.items = self.items.next
        else:
            trailer.next = probe.next

        # Decrement the logical size
        self.size -= 1