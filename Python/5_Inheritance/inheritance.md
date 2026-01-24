# Inheritance

Abstract Class
* Class that captures the common features and behavior of a set of related class
* Is not normally instantiated in client applications

Concrete Classes
* Classes that are actually used to create objects in client applications

Example:
    - Can move functions from LinkedBag and ArrayBag to AbstractBag

Overall Inheritance

Abstract Collection
|   -   AbstractBag
|       |   -   ArrayBag
|       |       |   -   ArraySortedBag
|       |       |       |   -   ArraySortedSet
|       |       |   
|       |       |   -   ArraySet
|       |
|       |   -   HashBag
|       |       |   -   Hash Set
|       | 
|       |   -   LinkedBag
|       |       |   -   LinkedSet
|       | 
|       |   -   TreeSortedBag
|       |       |   -   TreeSortedSet
|
|   -   AbstractDict
|       |   -   ArrayDict
|       |       |   -   ArraySortedDict
|       |
|       |   -   HashDict
|       |
|       |   -   LinkedDict
|       |
|       |   -   TreeSortedDict
|
|   -   AbstractList
|       |   -   ArraySortedList
|       |       |   -   ArrayList
|       |
|       |   -   LinkedList
|
|   -   AbstractStack
|       |   -   ArrayStack
|       |   -   LinkedStack
|
|   -   ArrayQueue
|   -   LinkedQueue
|       |   -   LinkedPriorityQueue
|
|   -   ArrayHeap
|   -   HeapPriorityQueue
|   -   LinkedBST
|   -   LinkedDirectedGraph
