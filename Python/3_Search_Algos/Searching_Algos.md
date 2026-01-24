# Searching Algorithms

## Search for the minimum
- Python's min function
    - returns smallest item in a list
    - Alternative: return the index of min item

- Steps:
    1. Treat first item as min
    2. Search from right to left for a item that is smaller
    3. If small item found, reset the position of the min item to the current position
    4. When algo reaches the end of the list, return the position of the min item
- O(n)


## Sequential Search of a List
- Python's in operator (__contains__ method)
    - Searches for a particular item within a list of arbitrarily arranged items.
- Steps
    1. Starts from left and goes to the right
    2. Each item is compared to the target, returning true if equal
    3. If end of list is passed, return false
- Complexity
    - Worst Case 
        - Item is not in list: O(n)
    - Best case
        - Item is in the first position: O(1)
    - Average Case
        - ((n) + (n - 1) + (n - 2) ... + 1) / 2 = O(n)


##  Binary Search of a Sorted List
-  Binary Search can be used on sorted data,

- Steps
    1. Start at the middle (assume list is sorted)
    2. Compare item at middle 
        - If item is less than target, repeat for lower half of the list
        - If item is greater than target, repeat for upper half of the list
    3. Repeat until item is found OR the left and right ends are inverted (left > right)

    4. Return -1 if item not found 

- Complexity: O(log(n))
    - Worst case: O(log2(n))
        - (item not in list)
        - n / 2^k       (bc your basically dividing the list 1/2 k times)
        - k = log2(n)


