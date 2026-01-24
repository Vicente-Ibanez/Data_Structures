# Taxonomy of Collections

Collections
|
| - Graph Collection
| - Hierarchical Collection
|   | - Binary Search Tree
|   | - Heap
|
| - Linear Collection
|   | - List
|   |   | - Sorted List
|   |
|   | - Queue
|   |   | - Priority Queue
|   |
|   | - Stack
|   | - String
|
| - Unordered Collection
    | - Bag
    |   | - Sorted Bag
    |
    | - Dictionary
    |   | - Sorted Dictionary
    |
    | - Set
        | - Sorted Set



Note: Taxonomy doesn't imply particular implementation of a collection.

# Categories of Operations on Collections

1. Determine Size
    - Use python's len function to obtain # of items in colelction.

2. Test of item membership
    - Use python's in operator to search for a given target item in the collection
    - Returns True if item found or false

3. Traverse the collection
    - Use python's for loop to visit each item in the collection
    - The order i nwhich the items are visited depends upon the type of collection

4. Obtain a string representation
    - Use Python's str function to obtain the string representation of the collection

5. Test of equality
    - Use python's == operator to determine if two collections are equal
    - Equal if they are the same type and contain the same items (the order in which piars of items are compared depends on the type of collection)

6. Concatenate two collections
    - Use python's + operator to obtain a new collection of the same type of the operands and containing the items in the two operands

7. Convert to another type

8. Insert an item

9. Remove an item

10. Replace an item

11. Access or retrieve an item

# Copying an item
1. Shallow copy
    - Items are not themselves coled before adding to the new list
    - instead mere references to these objects are copied (both collections point to the same items)

2. Deep Copy
    - Explicitly colones its items before adding them to the new collection

# Abstract Data Types (ADTs)
* From a user's perspective, a collection is an abstraction
    - Users only concerned with learning its interface (the methods available)
    - Developers are concerned with implementing a collection's behavior in the most efficient manner possible
        - Goal: to provide best perforamnce to users of the collections.
        - Underlying data structure can be different, but the interface is the same (List might have array or linked structure under it)