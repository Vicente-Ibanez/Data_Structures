# Queues
- Order collection of items

- FIFO (First in first out)
    - addition of new items happens at end
    - removal of eexisting items occurs at the front

- Examples
    * Grocery store lines
    * Printer (what gets sent to printer is added to printer's queue)

- Queue Abstract Data Type
    * Queue()
        - Creates new queue that is empty
        - It needs no parameters and returns an empty queue
    * Enqueue(item) 
        - Adds a new item to the rear of the queue
        - it needs the item and returns nothing
            - Depending on implentation, you can add to front or end
            - add to front: insert(0, item), add to end: append(item)
                - Arrays:
                    insert is O(n) for arrays bc you need to shift items over, whereas append is O(1)
                - Linked Lists:
                    insert is O(1) bc you just change pointers, whereas append is O(n) bc you need to get to the end of the queue
                        - append can be O(1) if you have a tail pointer

    * Dequeue()
        - Removes the front item from the queue
        - It needs no parameters and returns the item
        - The queue is modified
    * is_empty()
        - Tests to see whether the queue is empty
        - It needs no parameters and returns a boolean value
    * size()
        - returns the # of items in the queue
        - It needs no parameters and returns an integer
    * __len__()
    * __iter__()
    * __contains__()
    * __add__()
        - Combines 2 queues
    * clear()
    * peek()

## Linked Implementation of Queues

* Similar to linked stack
* Uses singly linked node class
        - pop removes first node
        - add is at tail
    - 2 external pointers
        * front (points to head)
        * rear (points to tail)
    - Given initial value of none
    - Add operation
        * Creates a new node
        * Sets pointer of last node to the new node
        * Set variable rear to the new nodes

### Linked Imp. Adding item to rear

Step 1: Create new node

         +---+    +------+    +------+    +------+
Front    |  -|--> | a | -|->  | b | -|->  | c | \| 
         +---+    +------+    +------+    +------+
                                              ^
                                              |
Rear -----------------------------------------┘      

         +---+      +------+
New node |  -|-->   | d | \| 
         +---+      +------+

Step 2: Set rear next to new node
         +---+    +------+    +------+    +------+      +------+
Front    |  -|--> | a | -|->  | b | -|->  | c | -|-->   | d | \| 
         +---+    +------+    +------+    +------+      +------+
                                              ^            ^ 
                                              |            |
Rear -----------------------------------------┘          +---+     
                                                         | | | 
                                                         +---+      
                                                        New node


Step 2: Set rear next the new node
         +---+    +------+    +------+    +------+      +------+
Front    |  -|--> | a | -|->  | b | -|->  | c | -|-->   | d | \| 
         +---+    +------+    +------+    +------+      +------+
                                                           ^ 
                                                           |
Rear ------------------------------------------------------┘           
                                                        

## Array Implementation
- Issue: Accessing head and tail in an efficient manner is complex

- Solution: Circular Aray Implementation
    * Can get good runtimes for both add & pop

    * Front and rear pointers
        - Start at begninning of array
        - Front "chases" rear through array 
    
    * Add operation
        - rear pointer moves farther ahead of the front pointer

    * Pop operation
        - Front pointer catches up by one position

    * When either pointer are about to run off the array
        - that pointer is reset to 0 index
        - essentially wraps the queue around to the beginning of the array
            - w/o cost of moving items

    Example:
                            Front     Rear
                              |        |
        Before enqueue: [ , , A, B, C, D]

                       Rear  Front
                         |    |
        After Enqueue:  [E, , A, B, C, D]


    * Max runtime of both add and pop are O(1)

    * When count = size of array
        - Resize array
        - populate front at the start of the array

        Steps:
            1. Create new array 2x size
            2. Iterate through queue
                - Copy items to new array
                - Start at position 0 in new array
            
            3. Reset items variable to the new array

            4. Set 
                - front to 0 
                - rear to queue's length-1

    * Pop:
        - Don't shift items to the left

        Example:
                            Front     Rear
                              |        |
        Before dequeue: [ , , A, B, C, D]

                               Front  Rear
                                 |     |
        After dequeue:  [ , ,  , B, C, D]


## Time and Space Analysis

Linked
    Time Complexity
    * O(n)
        * Uses a for loop
            * __str__()
            * __add__()
            * __eq__()

    Space Complexity
    * 2n+3
        - n = siace of queue
        - 3 data values, rear, head, size
        - 2n bc the data and reference to next node

Array
    Time Complexity
    * O(n)
        * Uses a for loop
            * __str__()
            * __add__()
            * __eq__()  
    * O(1) 
        * All else
        * Nothing is shifted in array from add and pop
        * Add/Pop
            - Jump to O(n)
            - if array is dynamic (upon resizing)
            - but average runtime of O(1)

    Space Complexity
    * Depends on load factor
        - Load Factor > 1/2 
            - Array more memory efficent than linked
        - Load Factor < 1/2
            - Less efficient


## Priority Queues
* Special type of queue
    - When items added to queue
        - they are assigned an order of rank
    - When removed 
        - Items of higher priority are removed before those of lower

    Items of same priority
        - FIFO
    
    If items cant be naturally compared
        - Create a wrapper class taht
            * Stores data
            * Stored priority

    2 Implementations of a priority queue
        1. Sorted List
        2. Trees --> Heaps

* Sorted List
    - List of comparable elemtns
    - Maintained in natural order
        - Min item should be always accessible at one end of the list
        - Elements inserted in proper place in the order

    - Singly linked structure
        - Represents this well if min item is always removed from the head of the structure
        - can inherit from LinkedQueue
            * Just change add() implementation

    - Add Implementation O(n)
        * Conducts search from new item's position in the list
        * Consider these cases
            1. Queue is empty
                - OR new item is larger or equal to item at the end
                - Add it at the rear
            
            2. Otherwise
                - Begin at head and move forward through the nodes until item is less than current node
                    - insert between current and previous nodes

                    - Trailer points to the new node
                        - new node points to probe

                        - if its the first node
                            - point head to new node and new node to probe

            




