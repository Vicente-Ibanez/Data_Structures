
def binary_search_recursive_helper(array:list, left: int, right:int, target:int):
    """ Helper function that recursively search a sorted array for a value.
    """
    if(left > right):
        return -1 # base case when the search window is empty, target is not in array
    
    mid = left + (right - left) // 2 # calculate the mid of the array to compare to target

    if (array[mid] == target): # if mid equals the target, return that position as target is found
        return mid
    elif (array[mid] < target): # if mid is less than target, recursively search the right half of the array
        return binary_search_recursive_helper(array, mid+1, right, target)
    else: # else, mid is greater than the target, recursively search the left half of the array
        return binary_search_recursive_helper(array, left, mid-1, target)
    

def binary_search_recursive(array:list, target:int):
    """ User facing function to avoid user passing parameters that can be calculated.
    """
    return binary_search_recursive_helper(array, 0, len(array)-1, target)

if __name__ == "__main__":
    l = [3, 7, 12, 23, 31] 
    print(binary_search_recursive(l, 23)) # prints 3
    print(binary_search_recursive(l, 10)) # prints -1
    print()

    l = [0, 1, 2, 3, 4, 5, 6] 
    print(f"List: {l}")
    print(f"Position of 5 (should be 5): {binary_search_recursive(l, 5)}")
    print(f"Position of 7 (not in array): {binary_search_recursive(l, 7)}")
    print(f"Position of -5 (not in array): {binary_search_recursive(l, -5)}")