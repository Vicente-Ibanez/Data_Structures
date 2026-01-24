def binary_search(target, sorted_lyst):
    """ Returns the position of target in sorted_lyst.
        If target is not in sorted_lyst, returns -1.
        
        Complexity: O(log n), where n is the number of elements in sorted_lyst.
        
    """
    left = 0
    right = len(sorted_lyst) - 1

    while left <= right:
        mid = (left+right) // 2
        
        if target == sorted_lyst[mid]:
            return mid
        elif target < sorted_lyst[mid]:
            right = mid - 1
        else:
            left = mid + 1
    return -1