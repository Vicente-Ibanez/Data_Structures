class Node(object):
    """A node in a linked structure."""
    def __init__(self, data=None, next=None):
        """Initialize a node with data and a reference to the next node.

        Args:
            data: The data to be stored in the node.
            next_node (Node): A reference to the next node in the structure.
        """
        self.data = data
        self.next_node = next