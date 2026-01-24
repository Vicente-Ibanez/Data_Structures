from array_bag import ArrayBag

class ArraySortedBag(ArrayBag):
    """An array-based sorted bag implementation."""

    def __init__(self, source_collection=None):
        """Sets the initial state of self, which includes the contents of
        source_collection, if it's present.
        """
        ArrayBag.__init__(self, source_collection)

    def __contains__(self, item):
        """Returns True if item is in self, or False otherwise."""
        # Use binary search for efficiency
        left = 0
        right = len(self) - 1
        while left <= right:
            mid_point = (left+right)//2

            if self.items[mid_point] == item:
                return True
            elif self.items[mid_point] > item:
                right = mid_point - 1
            else:
                left = mid_point + 1
            return False

    def add(self, item):
        """Adds item to self."""
        if self.is_empty() or item >= self.items[len(self)-1]:
            ArrayBag.add(self, item)

        else:
            # Resize the array if it is full
            if len(self) == len(self.items):
                self.resize(2 * len(self.items))
            
            # Search for first i tem >= new item
            target_index = 0
            while item > self.items[target_index]:
                target_index += 1

            # Open a hole for new item
            for i in range(len(self), target_index, -1):
                self.items[i] = self.items[i-1]
            
            # Insert item and update size
            self.items[target_index] = item
            self.size += 1

        def __add__(self, other):
            """Combines two sorted bags."""
            result = ArraySortedBag(self)
            for item in other:
                result.add(item)
            return result
