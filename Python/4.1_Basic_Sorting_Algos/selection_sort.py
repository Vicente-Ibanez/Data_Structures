from swap import swap

def section_sort(lyst):
    """
    Sorts a list using the selection sort algorithm.
    :param lyst: List of elements to be sorted
    :return: Sorted list
    """
    i = 0
    while i < len(lyst) - 1: # repeat from 1 to n - 1
        min_index = i # assume the minimum is the first element
        j = i + 1 # start the search from 1 after the last start
        
        while j < len(lyst): # Start search
            if lyst[j] < lyst[min_index]: # found new minimum
                min_index = j # update min_index
            j += 1

        if min_index != i: # Exchange needed
            swap(lyst, i, min_index)
        i += 1
    