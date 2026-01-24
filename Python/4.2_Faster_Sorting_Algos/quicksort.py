from .swap import swap
import random 

def quicksort(lyst):
    """ Sorts list in place using the quicksort algorithm.
        Main function that calls resursive helper so that it's easy to use the API.
    """

    quicksort_helper(lyst, 0, len(lyst) - 1)


def quicksort_helper(lyst, left, right):
    """ Recursive helper function for quicksort algorithm."""
    if left < right:
        # Perform the partitioning step for lyst
        pivot_location = partition(lyst, left, right)

        # Perform partitioning step for left sublist
        quicksort_helper(lyst, left, pivot_location - 1)

        # Perform partitioning step for right sublist    
        quicksort_helper(lyst, pivot_location + 1, right)

def partition(lyst, left, right):
    """ Partitions lyst into two sublists around a pivot value.
        All elements less than or equal to the pivot are moved to its left,
        and all elements greater than the pivot are moved to its right.
        Returns the final index of the pivot value.
    """
    # pivot is chose to be the middle of lyst, can be use other selection methods
    middle = (left + right) // 2 
    pivot = lyst[middle]
    
    # Swap the last item with the current pivot (putting the pivot at the end)
    lyst[middle] = lyst[right]
    lyst[right] = pivot

    # Set boundary point to the first position
    boundary = left

    # Move items less than the pivot to the left of the boundary
    for index in range(left, right):
        if lyst[index] < pivot: # item is less than pivot
            swap(lyst, index, boundary)
            boundary += 1 # move boundary over by one when an item less than pivot is found


    # Exchange the pivot item and the boundary item once the partitioning is finished
    swap(lyst, right, boundary)

    return boundary
        


def main(size=20, sort=quicksort):
    """ Main function to test quicksort algorithm."""
    lyst = [random.randint(1, size+1) for _ in range(size)]
    print("Unsorted list:", lyst)
    
    sort(lyst)
    
    print("Sorted list:", lyst)

if __name__ == "__main__":
    main()