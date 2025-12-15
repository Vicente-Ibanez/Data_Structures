# Arrays

Arrays have Random Access and Contiguous Memory.

Random Access:
* Computer obtains location of ith item by performing a constant # of steps.
    * No matter how large the array is, it takes the same amount of time to access any item.
* Steps:
    1. Fetch the base address of the array's memory block.
        - Base Address: machine address of the first item
    2. Return the results of adding the index to this address
        - Offset: Item's offset = index * constant (that represents # of memory in cells, in python = 1)
    ex: array's memory block: 10011101(base 2), each item requires a single cell of memory. Address of data at index 2 is 2(base 10) + 10011101(base 2) = 10011111(base 2).


Contiguous Memory
* Memory in which each data value in a data structure is physically adjacent to other data values in a same structures.

Benefit
* Constant lookup time (index function) / no searching for item as position

Downside
* Memory must be contiguous

Dynamic Array vs Static
Dynamic: Changes size, size not known until run time. User can specifcy length of dynamic array during instantiation.

Static
* Length/Capacity was determined at compile time
* Programmer needed to specify size with a constant
* Couldn't change length at run time, needed to predict memory usage.

Physical Size vs Logical Size

Physical Size
* Total # of array cells, or # used to specify its capacity when array is created

Logical Size
* num of items in array that should be currently available to the application

1) Array Methods
* Increasing Size of An Array
1. Create a new larger array
2. Copy the data from the old array to the new array
3. Reset the old array variable to the new array object

Runtime performance of adding n items to the array is O(n^2)
* 1 + 2 + 3 + ... + n = n(n+1)/2

To improve: double the array size to achieve average of O(n)


2) Decreasing size of array
1. Create a new smaller array
2. Copy the data from old array to new array
3. Reset the old array variable to the new array object

3) Insertion
1. Check for avaiable space before attempting insert
    - Increase physical size of array if necessary
2. Shift items from logical end of array to target index position down by one.
    - This opens a hole for the new item at the target index.
3. Assign the new item to the target index position
4. Increment the logical size by one

ex: insert D5 at Index 1
    D1, D2, D3, D4, __
    D1, D2, D3, D4, D4
    D1, D2, D3, D3, D4
    D1, D2, D2, D3, D4
    D1, D5, D2, D3, D4

Performance: Linear on average

4) Removing an item 
1. Shift the items from the one following the target index position to the logical end of the array up by one
    - Process closes the hole left by the removed item at the target index
2. Decrement the logical size by one.
3. Check for wasted space and decrease the physical size of the array if necessary

ex: remove D2 
    D1, D2, D3, D4, D5
    D1, D3, D3, D4, D5
    D1, D3, D4, D4, D5  
    D1, D3, D4, D5, D5
    D1, D3, D4, D5, __

Performance: Linear on average


## Running time of Array Operations
Operation	                Running Time
Access at ith position	    O(1), best and worst cases
Replacement at ith position	O(1), best and worst cases
Insert at logical end	    O(1), average case
Insert at ith position	    O(n), average case
Remove from ith position	O(n), average case
Increase capacity	        O(n), best and worst cases
Decrease capacity	        O(n), best and worst cases
Remove from logical end	    O(1), average case
Insert at ith position	    O(n), average case
Remove from ith position	O(n), average case
Increase capacity	        O(n), best and worst cases
Decrease Capacity	        O(n), best and worst cases

Overall
* Provides fast access to any item already present
* Provides fast insertions and removals at the logical last position
* Insertions / Removals at other positions are slower by order of magnitude
* Resizing takes linear time
    - but doubling size or halving minimizes # of times this must be done
* Can shrink when load factor in below 0.25 to get better performance