# Faster Sorting Algorithms
    - Previous algos were all O(n^2) is worst and average cases
    - Can get O(nlogn) with Divide-and-Conquer Strategy
        - These algos break list into smaller sublists
        - Sublists are sorted Recursively
            - # of sublists is logn
            - amount of work to rearrange data in sublists is n
                --> Final recursive time is nlogn


NOTE:
    - These algos use 3 functions
        1. The function that the user calls
            - this makes it so the user just passes the list and doen't have to worry about any other args
                ex: quicksort(lyst), merge_sort(lyst)

        2. The function that is used for the recursive calls
            - this is called by the 1st function and by itself
            - Hides the exrtra parameters required by recusrive calls
                ex: quicksort_helper(lyst, left, right)

        3. The function that does a modification of the list
            ex: partition(lyst, left, right)



## Quicksort
    - Sort algo that selects a pivot item in a list
        - Moves smaller items to the pivot's left 
        - Moves larger items to the pivot's right
    - Recursively sorts the resulting sublists

- Steps:
    1. Begin by selecting the item at the list's midpoint
        - this item is called hte pivot
        - different ways to choose the pivot

    2. Parition items in the list so that all items 
        - less than the pivot are moved to the left of the pivot
        - rest are moved to its right
        
        - Final position of the pivot itself varies (depending on actual items involved)

            - ex: the pivot ends up being 
                - rightmost in the list if it is the largest item
                - left most if it is the smallest

                - Wherever pivot endsup is it's final position when the list is fully sorted

    3. Divide and conquer  
        - Reapply the process recursively to the sublists formed by splitting the list at the pivot
            - One sublist consists of all items to the left of the pivot (smaller items)
            - the other sublist has all items to the right (larger ones)

    4. Process terminates each time it encounters a sublist with fewer than 2 items.

- Paritioning
    - Most complicated part of algo is operation of parititoning the items in a sublist
    - 2 principal ways to do this

    Easier method:
        1. Swap the pivot with the last item in the sublist
        
        2. Establish a boundary between the items known to be less than the pivot and the rest of the items
            - initially this boundary is positioned immediately before the first item

        3. Start with the first item in the sublist after the boundary
            - scan across the sublist
            - Every time you encounter an item less than the pivot, swap it w/ the first item after the boundary
            - Advance the boundary

        4. Finish by swapping the pivot w/ the first item after the boundary

- Example:

    Unsorted List:          12  19  17  18  14  11  15  13  16
    Pivot (14)

    1. Swap pvit with       12  19  17  18  16* 11  15  13  14*
        the last item

    2. Establish        ... 12  19  17  18  16  11  15  13  14
        boundary before 
        the first item

    ----------------
    3. Scan for the     ... 12< 19  17  18  16  11  15  13  14
        first item less
        than the pivot

    4. Swap this item   ... 12  19  17  18  16  11  15  13  14
        with the first
        item after the
        boundary.
        (here 12 is
        swapped w/ 12)

    5. Advance the      12  ... 19  17  18  16  11  15  13  14
        boundary

    ----------------
    6. Scan for the     12  ... 19  17  18  16  11< 15  13  14
        next item 
        less than 
        the pivot

    7. Swap this item   12  ... 11* 17  18  16  19* 15  13  14
        with the first
        item after the 
        boundary

    8. Advance the      12  11  ... 17  18  16  19  15  13  14
        boundary

    ----------------
    9. Scan for the     12  11  ... 17  18  16  19  15  13< 14
        next item 
        less than 
        the pivot

    10. Swap this item  12  11  ... 13* 18  16  19  15  17* 14
        with the first
        item after the 
        boundary

    11. Advance the     12  11  13  ... 17  18  16  19  15  14
        boundary

    ----------------
    12. Scan for the    12  11  13  ... 17  18  16  19  15  14
        next item 
        less than the
        pivot, however
        there is not
        one.

    13. Interchange the pivot with the first
        item after the boundary
        - now, all items less than the 
            pivot are to the pivot's left
            and the right are to the right

                        12  11  13  ... 14* 18  16  19  15  17*

    ----------------
    14. Reapply process to both left and right of pivot

    List segment:                   Pivot Item
    12 19 16 18 14 11 15 13 16      14
    12 11 13                        11
    13 12                           13
    12

    16 19 15 17 18                  15
    19 18 17 16                     18
    16 17                           16
    17
    19
        
    
- Complexity Analysis of Quicksort
    - During first parition operation
        * You'll scam all items from the beginning of the list to its end
        * O(n)

    - Work after partition is = length of left and right partitions
        - O(n-1)

    - After 2nd partitioning, work is = to length of four pieces
        - length is about = n
        - work is proporitional to n yet again
    
    - As list is divided into more pieces
        - total work remain proportional to n

    - How many times is the list partitioned:
            --> Best case: O(nlogn) 
                - Optimistic assumption: each partition is 50/50 split
                - you then will split O(nlogn)
        
        

            --> Worst case: O(n^2)
                - list is already sorted
                    - pivot is at one end of the 
                    - No elements are exchanged
                - Total # of partitions = n-1
                - Total # of comparisons performed = (1/2)n^2 - (1/2)n = O(n^2)

            
        - Memory Usage: 
            --> BC & WC: O(logn) 

                - Each recursive call required constant amount of memory for a stack frame
                    - there a 2 recursive calls after each partition 


        Notes:
            - Worst case perforamnce is rare
            - Choosing pivot can approximate average case to O(nlogn)
                * Select pivot at random
                * Choose median of first, middle, and last



## Merge Sort
    - Employs recursive divide-and-conquer strategy to break the O(n^2) barrier

- Steps:
    1. Compute the middle position of a list 
        - recursively sort its left and right sublists (divide and conquer)
    
    2. Merge the two sorted sublists back into a single sorted list

    3. Stop the process when sublists can no longer be subdivided

- Implementing the merge process
    * Merging process uses an array of the same size as the list (copy_buffer)
        - to avoid overhead of allocating and deallocating the copy_buffer each time merge is called
            --> buffer is allocated once in mergesort function and passed as an arg to mergesort_helper and merge

    * Each time merge is called
        - it needs to know the bounds of the sublist 
            with which it is working
        - low/high
    
    * Merge function combine two sorted sbulists into a larger sorted sublist
        - first sublist lies between low and middle
        - second between middle+1 and high

        - Process consists of 3 steps
            1. Step up index pointers to the first items in each sublist
                - these are at positions low and middle + 1
            
            2. Starting w/ the first item in each sublist, repeatdly compare items
                - Copy the smaller item from its sublist to the copy buffer and advance to the next item in the sublist
                - Repeat until all items have been copied from both sublists
                - If the end of one sublist is reached before the others
                    - Finish by copying the remaining items from the other sublist

            3. Copy the portion of copy buffer between low and high back to the corresponding positions in lyst

    - Notes:
        - if sublists are evenly subdivided at each level
            --> there will be 2^k sublists to be merged at level k
        - had the initial list not been a power of 2
            --> then an exactly even subdivision would not have been achieved at each level
            --> aand the last level would not have contained all full complement of sublists

- Example:
    Sublists generated during call of merge sort helper

    Level 0        4    1   7   6   5   3   8   2
                            <<<<    >>>>
    Level 1     4   1   7   6           5   3   8   2
                   <<   >>                 <<   >>
    Level 2   4  1          7  6     5  3           8  2
              <  >          <  >     <  >           <  >
    Level 3 4      1      7     6   5     3       8       2


    Merging the sublists generated during a merge sort

    Level 3  4     1      7     6   5     3       8       2
              >   <        >   <     >   <          >    <
    Level 2    1 4          6 7       3 5             2 8
                  >>      <<              >>       <<
    Level 1         1 4 6 7                  2 3 5 8
                          >>>>            <<<<
    Level 0                  1 2 3 4 5 6 7 8 





- Complexity Analysis: BC, WC, AC: O(nlogn)
    - 2 for loops
        - each which loops (high-low + 1) times
        - therfore function's running time is O(high - low)
            - and all merges at a single level take O(n) time
        - Since merge sort helper splits sublists as evenly as possible at each level
            --> # of levels is O(logn)
            --> max running time for this function is O(nlogn) in all cases

    - Space requirements: O(nlogn)
        --> O(logn) required on the call stack to support recursive calls
        --> O(n) space used by copy buffer
