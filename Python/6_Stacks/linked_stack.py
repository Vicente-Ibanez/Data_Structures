fron node import Node
from abstract_stack import AbstractStack

class LinkedStack(AbstractStack):
    """ A linked-list-based stack implementation """

    def __init__(self, source_collection=None):
        self.items = None
        AbstractStack.__init__(self, source_collection)

    # Accessor methods
    def __iter__(self):
        """ Supports iteration over a view of self.
         Visits items from bottom to top of stack """
        
        def visit_nodes(node):
            if node != None:
                visit_nodes(node.next)
                temp_list.append(node.data)

            temp_list = list()
            visit_nodes(self.items)
            return iter(temp_list)
        
    def peek(self):
        """ Returns the item at top of the stack
        Precon: the stack is not empty
        Raises KeyError if the stack is empty """
        
        if self.is_empty():
            raise KeyError("The stack is empty")
        return self.items.data
    
    # Mutator methods
    def clear(self):
        """ Makes self become empty """
        self.size = 0
        self.items = None

    def push(self, item):
        """ Inserts item at top of the stack """
        self.items = Node(item, self.items)
        self.size += 1

    def pop(self):
        """ Removes and returns the item at the top of the stack.
         Raises KeyError if the stack is empty """
        
        if self.is_empty():
            raise KeyError("The stack is empty")
        
        old_item = self.items.data
        self.items = self.items.next
        self.size -= 1
        return old_item