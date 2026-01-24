from swap import swap

def bubble_sort(lyst):
    """
    Sorts a list using the bubble sort algorithm.
    :param lyst: List of elements to be sorted
    :return: Sorted list
    """
    n = len(lyst)
    
    while n > 1: # Do n-1 bubbles
        i = 1

        while i < n:
            if lyst[i] < lyst[i-1]: # Compare current item to previous 
                swap(lyst, i, i-1)
            
            i += 1 # Continue to next pair of items
        n -= 1 # One less item to check each time at the end

    return lyst

def bubble_sort_with_tweek(lyst):
    """
    Sorts a list using the bubble sort algorithm with an optimization.
    :param lyst: List of elements to be sorted
    :return: Sorted list
    """
    n = len(lyst)
    
    while n > 1: # Do n-1 bubbles
        swapped = False
        i = 1 # start at the 1st position and compare to previous

        while i < n: #while there's still comparisons to be made
            if lyst[i] < lyst[i-1]:
                swap(lyst, i, i-1)
                swapped = True
            i += 1 # Continue to next pair of items

        if not swapped: # If no swaps were made, the list is sorted
            return lyst
        
        n -= 1 # One less item to check each time at the end
        
        