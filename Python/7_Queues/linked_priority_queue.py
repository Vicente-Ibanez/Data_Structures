"""
File: linkedpriorityqueue.py
"""

from node import Node
from linked_queue import LinkedQueue

class LinkedPriorityQueue(LinkedQueue):
    """A link-based priority queue implementation."""


    def __init__(self, source_collection = None):
        """Sets the initial state of self, which includes the
        contents of sourceCollection, if it's present."""
        LinkedQueue.__init__(self, source_collection)

    def add(self, item):
        """Adds item to its proper place in the queue."""
        if self.is_empty() or item >= self.rear.data:
            LinkedQueue.add(self, item)
        else:
            probe = self.front
            trailer = None
            while item >= probe.data:
                trailer = probe
                probe = probe.next
            new_node = Node(item, probe)
            if trailer is None:
                self.front = new_node
            else:
                trailer.next = new_node
            self.size += 1