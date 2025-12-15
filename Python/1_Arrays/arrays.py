class Array(object):
    """Represents an array data structure."""

    def __init__(self, capacity, fill_value=None):
        """Initialize the array with a given capacity and fill value."""
        DEFAULT_CAPACITY = 10
        
        self.items = list()
        for count in range(DEFAULT_CAPACITY):
            self.items.append(fill_value)

    def __len__(self):
        """Return the length of the array."""
        return len(self.items)
    
    def __str__(self):
        """Return a string representation of the array."""
        return str(self.items)
    
    def __iter__(self):
        """Return an iterator for the array."""
        return iter(self.items)
    
    def __getitem__(self, index):
        """Return the item at the given index."""
        return self.items[index]
    
    def __setitem__(self, index, value):
        """Set the item at the given index to the specified value."""
        self.items[index] = value
    
    def __resize__(self):
        """Resize the array to double its current capacity."""
       
        if self.logical_size == len(self): 
            temp = Array(len(self) * 2)         # Create new array
            for i in range(self.logical_size):  # Copy data from the old array to the new array
                temp[i] = self.items[i]         
            
            self.items = temp.items             # Reset the old array variable to the new array

    def __decrease_size__(self):
        """Decrease the size of the array to half its current capacity."""
        
        if self.logical_size <= len(self) / 4 and len(self) >= self.DEFAULT_CAPACITY*2:
            temp = Array(len(self) // 2)       # Create new array
            for i in range(self.logical_size):  # Copy data from the old array to the new array
                temp[i] = self.items[i]
            
            self.items = temp.items             # Reset the old array variable to the new array

    def insert(self, target_index, new_item):
        """Insert a value at the specified index."""
        self.__resize__() # Increase size if necessary

        # Shift items down by one position
        for i in range(self.logical_size, target_index, -1):
            self.items[i] = self.items[i - 1]

        # Add new item and increment logical size
        self.items[target_index] = new_item
        self.logical_size += 1

    def remove(self, target_index):
        """Remove and return the item at the specified index."""
        # Shift items up by one position
        for i in range(target_index, self.logical_size - 1):
            self.items[i] = self.items[i + 1]
        
        # Decrement logical size
        self.logical_size -= 1

        #Decrease size if necessary
        self.__decrease_size__()
        