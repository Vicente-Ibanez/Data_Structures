class BagInterface(object):
    """Interface for all bag types"""
    
    # Constructor
    def __init__(self, source_collection=None):
        pass

    # Accessor methods
    def is_empty(self):
        """Returns True if len(self) == 0"""
        return True
    
    def __len__(self):
        """Returns number of items in self"""
        return 0
    
    def __str__(self):
        """Returns string representation of self"""
        return ""
    
    def __add__(self, other):
        """ Returns a new bag containing the contents of self and other """
        return None
    
    def __eq__(self, other):
        """ Returns True if self and other contain the same items """
        return False
    
    def count(self, item):
        """Returns number of occurrences of item in self"""
        return 0
    
    # Mutator methods

    def clear(self):
        """Makes self become empty"""
        pass

    def add(self, item):
        """Adds item to self"""
        pass

    def remove(self, item):
        """Removes and returns an instance of item from self
        Raises KeyError if item not in self"""
        pass