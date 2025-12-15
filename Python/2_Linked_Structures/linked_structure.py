from node import Node

class Linked_Structure(object):
    
    def __init__(self, collection=None):
        """Initialize an empty linked structure."""
        self.head = None

        if collection:
            for count in range(0, len(collection)):
                pass


    # Traversal
    def traverse(self):
        """Traverse the linked structure and yield each node's data."""
        probe = self.head
        while probe is not None:
            # do process
            probe = probe.next_node

    # Searching
    def search(self, target_item):
        """Search for the first node containing the target data.

        Args:
            target: The data to search for in the linked structure.

        Returns:
            The node containing the target data, or None if not found.
        """
        probe = self.head
        # loop until we find the target item or reach the end of the structure
        while probe is not None and target_item != probe.data:
            probe = probe.next

        if probe != None: # Target item found
            return probe
        else:
            return None # Target item not in structure
            
    def __getitem__(self, index):
        """Get the data at the specified index in the linked structure.

        Args:
            index (int): The index of the node to retrieve.
        """
        if index < 0:
            raise IndexError("Index cannot be negative.")

        if index > len(self) - 1:
            raise IndexError("Index out of range.")
        
        probe = self.head

        while index > 0:
            probe = probe.next
            index -= 1
        return probe.data

    def replace(self, target_item, new_item):
        """Replace a specific item new data.

        Args:
            index (int): The index of the node to replace.
            new_item: The new data to be stored in the node.
        """
        probe = self.head

        while probe != None and target_item != probe.data:
            probe = probe.next
        if probe != None:
            probe.data = new_item
            return True
        else:
            return False
        

    def __setitem__(self, index, new_item):
        """Replace the data at the specified index with new data.

        Args:
            index (int): The index of the node to replace.
            new_item: The new data to be stored in the node.
        """
        if index < 0:
            raise IndexError("Index cannot be negative.")

        if index > len(self) - 1:
            raise IndexError("Index out of range.")
        
        probe = self.head

        while index > 0:
            probe = probe.next
            index -= 1
        probe.data = new_item

    def push(self, new_item):
        """Push a new item onto the front of the linked structure.

        Args:
            new_item: The data to be stored in the new node.
        """
        new_node = Node(new_item, self.head)
        self.head = new_node

    def append(self, new_item):
        """Append a new item to the end of the linked structure.

        Args:
            new_item: The data to be stored in the new node.
        """
        new_node = Node(new_item)

        if self.head is None:
            self.head = new_node
        else:
            probe = self.head
            while probe.next_node != None:
                probe = probe.next_node

            probe.next_node = new_node
    
    def pop(self):
        """Pop the first item from the linked structure.

        Returns:
            The data from the removed node.
        """
        if self.head is None:
            raise IndexError("Pop from empty linked structure.")

        popped_node = self.head
        self.head = self.head.next_node
        return popped_node.data