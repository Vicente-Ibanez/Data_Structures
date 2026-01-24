def sequentialSearch(target, lyst):
    """ Returns the position of target in lyst.
        If target is not in lyst, returns -1.
        
        Complexity: O(n), where n is the number of elements in lyst.
        
    """
    position = 0
    while position < len(lyst):
        if target == lyst[position]:
            return position
        position += 1
    return -1