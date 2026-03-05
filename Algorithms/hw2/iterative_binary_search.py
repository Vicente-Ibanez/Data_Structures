
def iterative_binary_search(array: list, target: int) -> int:
    """ This function is the iterative version of binary search
        The midpoint of the array is compared to the target item.
        Depending on the if the mid value is less or more than the target,
        the search window is adjusted accordingly.
    """
    # Get the middle index of the array so it can be compared to the target item
    # do len() - 1 because python lists starts at index 0.
    # do // because the mid index needs to be a whole integer
    left = 0
    right = len(array) - 1

    while left <= right: # repeat until the search window is empty
        
        mid = left + (right - left) // 2 # calculate mid for the adjusted search window

        if array[mid] == target:  # if the mid equals the target, return that index 
            return mid
        elif array[mid] > left: # if the mid is greater than the target, shift the left hand side up to mid + 1
            left = mid + 1      # it's mid + 1 because we already checked mid against target
        else:                   # else, mid is less thann target, so shift right hand side down to mid - 1
            right = mid - 1     # it's mid + 1 because we already checked mid against target

    
    return -1 # return -1 if the code reaches this line, because the target was never found

if __name__ == "__main__":
    l = [0, 1, 2, 3, 4, 5, 6] 
    print(f"List: {l}")
    print(f"Position of 5 (should be 5): {iterative_binary_search(l, 5)}")
    print(f"Position of 7 (not in array): {iterative_binary_search(l, 7)}")
    print(f"Position of -5 (not in array): {iterative_binary_search(l, -5)}")


