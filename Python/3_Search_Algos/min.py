def index_of_minimum(lyst):
    """ Returns the index of the minimum element in lyst.
        If lyst is empty, returns -1.
        
        Complexity: O(n), where n is the number of elements in lyst. 
        (technically O(n-1) since first item is not compared)
        """
    if len(lyst) == 0:
        return -1

    min_index = 0
    current_index = 1

    while current_index < len(lyst):
        if lyst[current_index] < lyst[min_index]:
            min_index = current_index
        current_index += 1
    return min_index