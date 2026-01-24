from abstract_collection import AbstractCollection

class AbstractStack(AbstractCollection):
    """ An abstract stack implementation """

    # Constructor
    def __init__(self, source_collection=None):
        """ Sets the initial state of self, which includes
        the contents of source_collection, if it's present """
        AbstractCollection.__init__(self, source_collection)

    # Mutator methods
    def add(self, item):
        """ Adds item to the stack """
        self.push(item)