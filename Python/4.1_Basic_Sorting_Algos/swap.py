def swap(lyst, i,, j):
    """ Swaps the elements at indices i and j in lyst.
        
        Complexity: O(1)
        
    """
    temp = lyst[i]
    lyst[i] = lyst[j]
    lyst[j] = temp

    # lyst[i], lyst[j] = lyst[j], lyst[i]  # Alternative Pythonic way, but it's the same underneath