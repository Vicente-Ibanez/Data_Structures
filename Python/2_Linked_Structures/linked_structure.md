# Linked Structure
* Consists of items that are linked to other items.
* Last item has no link to other item (empty link)
* Represents linear sequence of items
* Cannot immediately access an item by specifying its index position
    - instead, progreammer must start at one end and follow the links until desired position is reached

Noncontiguous Memory
* Linked structure decouples the logical sequence of items in the structure from any ordering in memory
    - Cell for a given item can be found anywhere in memory (so long as computer can follow link to its address)

Node
* Basic unit of representation in linked structure
* Contains
1. Data Item
2. Link to next node
(3. link to previous in doubly linked)

- Nodes are instantiated with memory from object heap, and are returned to heap by garbage collection when it is no longer referenced.

Simplest linked structures:
Singly Linked Structure and Doubly Linked Structure

ex:
Singly: Head -> [D1, -]-> [D2, -]-> [D3, \]
Doubly: Head -> [\, D1, =]<=>[=, D2, =]<=>[=, D3, \]
        Tail ---------------------------------^

Singly
* Can only go in one direction
Doubly
* Can go in both directions
* has tail lnik

Benefit
* Insertion / Removal occurs without shifting data items in memory
    - one item found/insert position, modfication is instant
    - Linked Struct can be resized with no extra memory cost and no copying of data items


Other terms:
* Pointers
    - direct access to the address of data
* Object Heap
    - An area of memory from which storage for objects is dynamically allocated
    -  Programmer simply asks computer for a pointer to a new node from this noncontiguous memory (obj heap)
* References
    - python programmers set up nodes & linked structures by using references to objects

Operations
1. Sequential Search
    - 0(n) on average
    - Does not have random access
2. Replace / Set item
    - O(n) bc of linear search/traversal
3. Push item
    - O(1)
    - No need to copy or shift data, just create new node & change pointers
4. Append item
    - O(n)
    - Have to traverse to the end