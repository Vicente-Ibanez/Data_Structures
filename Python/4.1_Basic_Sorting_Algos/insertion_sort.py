from swap import swap

def insertion_sort(lyst):
    """
    Sorts a list using the insertion sort algorithm.
    :param lyst: List of elements to be sorted
    :return: Sorted list
    """
    
    i = 1 # start wit the first item
    while i < len(lyst): # repeat for each item in the list except for the last
        item_to_insert = lyst[i] # take the ith item
        # Compare it to all i-1 items to its left, going backwards (starting with i-1, then i-2, till 0)
        j = i - 1 
        while j >= 0: 
            if item_to_insert < lyst[j]:
                lyst[j+1] = lyst[j] # move current item in i-1 to the right
                j-=1 # continue looking to the left
            else:
                break # if we find an item smaller, we can stop looking
        
        lyst[j+1] = item_to_insert # insert the item in the correct position

        i += 1

    return lyst
            
        
