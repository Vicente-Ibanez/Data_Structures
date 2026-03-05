

def partition(array:list, low: int, high:int):
    """ 
    This function uses the first item as the pivot for the partition.
    It is possible to use other items for the partition.
    The pivot is used to sort the items. Items lower than the pivot
    are swapped with items that are higher, moving lower items
    to the left, and higher items to the right of the subarray. 
    Then the pivot is placed inbetween, which is its final spot.
    """
    pivot = array[low] # The first item in the subarray is chosen as the pivot

    # keeps track of which items can be swapped 
    # initialize as the pivot, since the varaible
    # is incremented before use
    available_to_swap = low 

    # iterate over the range from 
        # start: lower + 1 (item after the pivot)
        # end: high + 1: the last item in the range, 
            # it's +1 because range doesn't include last item
        # step: 1, as we increment i to be the next item each loop
    for i in range(low+1, high + 1, 1):

        # if the item is less than the pivot
        # move it to the left
        if array[i] < pivot: 
            # increment the swap position so that we swap the next
            # appropriate item
            available_to_swap += 1 
            # swap the items 
            array[i], array[available_to_swap] = array[available_to_swap], array[i]
    
    # swap the pivot with the next avaialbe position that can be swapped
    array[low], array[available_to_swap] = array[available_to_swap], array[low]
    
    return available_to_swap # return the pivot's final index position

def quick_sort_recursive(array, low, high):
    """
    This function recursively partitions the array.
    Each recursive call places the pivot item in the 
    correct, final spot, and moves the items to the
    correct side of the pivot.
    """
    if (low < high): #stop when there are no more pivots to place
        # The index where the pivot was place
        # which is used to split the array into subarrays 
        # that are to the left and right of the pivot
        p = partition(array, low, high) 

        quick_sort_recursive(array, low, p-1) # sort the subarray that is to the left of the pivot
        quick_sort_recursive(array, p+1, high) # sort the subarray that is to the right of the pivot

if __name__ == "__main__":
    # a = [3, 5, 1, 4, 2]
    a = [30, 10, 50, 20, 60, 40]
    quick_sort_recursive(a, 0, len(a) - 1) # subtract 1 from the length as python indexes from 0
    print(a)