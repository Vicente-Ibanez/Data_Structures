from .swap import swap
from .arrays import Array

def merge_sort(lyst):
    """ Function called by users to perform merge sort
    
    lyst: list being sorted
    copy buffer: Temporary spacen eeded during merge
    """

    copy_buffer = Array(len(lyst))
    merge_sort_helper(lyst, copy_buffer, 0, len(lyst) - 1)

def merge_sort_helper(lyst, copy_buffer, low, high):
    """ Recursive function for merge sort

        lyst: list being sorted
        copy buffer: temp space needed during merge
        low, high: bounds of sublist
        middle: midpoint of sublit
    """
    if low < high:
        middle = (low + high) // 2
        # Sort lower half of list
        merge_sort_helper(lyst, copy_buffer, low, middle)

        # Sort upper half of list
        merge_sort_helper(lyst, copy_buffer, middle+1, high)

        # Perform merge of list
        merge(lyst, copy_buffer, low, middle, high)


def merge(lyst, copy_buffer, low, middle, high):
    """ Function that performs the merge
    lyst:
    copy_buffer:
    low: beginning of first sorted sublist
    middle: end of first sorted sublist
    middle + 1: beginning of second sorted sublist
    high: end of second sorted sublist
    Initialize i1 and i2 to the first items in each sublist
    """

    i1 = low
    i2 = middle + 1

    # Interleave items from the sublist into the copy buffer
    # in such a way that order is maintained 

    for i in range(low, high+1):
        if i1 > middle:
            copy_buffer[i] = lyst[i2] # first sublist exhausted
        elif i2 > high:
            copy_buffer[i] = lyst[i1] # second sublist exhausted
            i1 += 1
        elif lyst[i1] < lyst[i2]:
            copy_buffer[i] = lyst[i1] # Item in first sublist < item in second sublist
            i1 += 1
        else:
            copy_buffer[i] = lyst[i2] # item in second sublist < item in first sublist
            i2 += 1
        
    for i in range(low, high + 1): # Copy sorted items back to 
        lyst[i] = copy_buffer[i]   # proper position in lyst

        

