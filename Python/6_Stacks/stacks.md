# Stacks
- Linear collections
- Restrict access to just one end (top)
    - LIFO Last-in First-Out

Operations:
* Push: Add to top
* Pop: Remove from Top

Useful for
- Translating infix expressions to postfix
- Evaluating postfix expressions
- Backtracking algorithms
- Managing Computer memory in support of function and method calls
- Supporting undo feature
- Maintaining a history of the links visited by a web browser

Stack Interface

is_empty()
len()
str()
iter()
contains()
s1.add(s2)
    - Same as (s1 + s2)
s.eq(obj)
    - Same as s ==
clear()
peek()
    - Look at item on top without popping
push(item)
    - Adds item to top of stack
pop()
    - Removes item from top of stack

## Balancing Brackets
Steps:
1. Scan across the expression
    - Pushing open brackets onto a stack
2. On encountering a closing bracket, if the stack is empty or if the item on the top of the stack is not an opeing bracket of the same time
    - you know the brackets do one balance
    - can quit process and signal expression is improperly formed
3. Otherwise, pop the item off the top of the stack and continue scanning the expression
4. When you reach the end of the expression
    - the stack should be empty
    - if it is not, you know the brackets do not balance


## Infix to Postfix Expressions

Examples:
Infix           Postfix         Value
34              34              34
34 + 22         34 22 +         56
34 + 22 * 2     34 22 2 * +     78
(34 + 22) * 2   34 22 + 2 *     112

Steps:

1. Scan across expression from left to right
2. On encountering an operator
    - apply it to the two preceeding operands and replace all three by the result
3. Continue scanning until you reach the expression's end
    - at which point only the expression's value remain

Algorithm: (token referns to operand or operator)

Create a new stack
While there are more tokens in the expression
    Get the next token
    If the token is an operand
        Push the operand onto the stack
    Else if the token is an operator
        pop the top 2 operands from the stack
        Apply the operator to the two operands just popped
        Push the resulting value onto the stack
Return the value at the top of the stack

Example: Postfix Expression: 4 5 6 * + 3 -	Resulting Value: 31

Portion of Postfix              	Operand Stack	        Comment
Expression Scanned So Far
-------------------------           ------------            ---------
No tokens have been scanned yet.    The stack is empty.
4	                                4	                    Push the operand 4.
4 5	                                4 5	                    Push the operand 5.
4 5 6	                            4 5 6	                Push the operand 6.
4 5 6 *	                            4 30	                Replace the top two operands by their product.
4 5 6 * +	                        34	                    Replace the top two operands by their sum.
4 5 6 * + 3	                        34 3	                Push the operand 3.
4 5 6 * + 3 -   	                31	                    Replace the top two operands by their difference.
                                    Pop the final value.

## Converting Infix to Postfix
Steps:
1. Start with an empty postfix expression and an empty stack
    - which will hold operators and left parentheses

2. Scan across the infix expression from left to right

3. On encountering an operand, append it to the postfix expression.

4. On encountering a left parenthesis, push it onto the stack

5. On encountering an operator
    - pop off the stack all opeartors that have equal or higher precedences
    - append them to the postfix expression
        - and then push the scanned operator onto the stack

6. On encountering a right parenthesis, shift operators from the stack to the postfix expression until meeting the matching left parenthesis, which is discarded

7. On encountering the end of the infix expression
    - transfer the remainin g operators from the stack to the postfix expression

## Backtracking Algorithm
    - Begins in predefined starting state
        - then moves from state to state in search of a desire ending state
    - At any point when theres a choice 
        - pick one 
    - When algo reaches an undesireable outback
        - back up to the last point at which there was an unexplored alternative and try it
    - algo either 
        - exhaustively searches all states
        - reaches the desired ending state

Pseudo Code:
    Create a new stack
    Push teh starting state onto the stack
    While the stack is not empty
        pop the stack and examine the state
        if the state represents an ending state
            return succecssful conclusion
        elif the state has not been visited
            mark the state as visited
            push onto the stack all unvisited 
    return unsuccessful conclusion


## Memory Management
- Computer's runtime system must keep track of various details that are invisible to the authors

Tasks:
- Associating variables with data objects stored in memory so they can be located when these variables are referenced
- Remembering the address of the instructions when that function or method finishes execution
- Allocating memory for a function's arguments and temporary variables
    - which exist only during the execution of that function

### Architecture of a run-time Environment (Python Virtual Machine PVM)

All Memory              Call Stack              Activation Record
----------              ----------              --------------------
Object Heap               |                     
----⌄---- encroaches      / Method n 
Unused Memory           /   Activation Record
----^---- encroaches  /     ------------      <-- basePtr
Call Stack          <       ...                   / Temporary Variables
----------            \     ----------           /  ----------
Modules and             \   Method 2            /   Parameters
class variables           \ Activation Record <     ----------
----------                | ----------          \   Return Address
Program                   | Method 1             \  ----------
(bytecode for             | Activation Record     \ Prev basePtr
all methods)              |                         ----------
----------                                          Return value
Python Virtual
Machine


Subroutine
    - Used for python function

Activation record
    - Chunk of memory containing storage for each function 
        - call's parameters
        - temporary variables
        - return value
        - return address


- Pythhon Virtual Machine (PVM)
    - executes a python program
    - internal to PVM are 2 variables
        1. locationCounter  
            * Points at the instructions the PVM will execute next
        2. basePtr
            * Points at the top activation record's base

- Bytecodes for all subroutines of the pgraom

- The prgoram's module and class variable

- The call stack
    * Everytime a subroutine is called
        - an activation record is created and pushed onto the call stack
        - when a subroutine finishes execution and returns control of the subroutine that called it
            - the activation record is popped off the stack
    * Total # of activation records on the stack = # of subroutine calls currently in various stages of exeuction

- Unused memory
    * This region's size grows and shrinks in response to the demand of the call stack and the object heap

- The object heap
    * In Python, all objects exist in a region of memory called the heap
        - When an object is instantiated, PVM must find space for the object on the heap
        - when object is no longer needed, PVM's garbage collector recovers the space for future use
            - When low on space, heap extends further into the region marked Unused Memory



Activation Records
* Contain 2 types of information
    1. Temporary Variables and Parameters
        - Hold data needed by the executing subroutine
    2. Remaining regions
        - Hold data that allow the PVM to pass control backward from currently executing subroutine to the subroutine that called it

When a subroutine is called, the PVM performs:
1. Creates the subroutine's activation record and pushes it onto the call stack
    - The activation record's bottom three regions are fixed in size
    - the top two vary depending on the number of parameters and local variables used by the subroutine

2. Saves the basePtr's current value in teh region labeled Prev basePtr
    - and sets the basePtr to the new activation record's base

3. Saves the location counter's current value in the region labeled Return Address
    - and sets the location counter to the first instruction of the called subroutine

4. Copies the calling parameters into the region labeled Parameters

5. Starts executing the called subroutine at the location indicated by the location counter

When subrouting is executing
    - adding an offset to the basePtr references temporary variables and paremeters in the activation record
        - thus, regardless of activation record's location in memory, you can. correctly access the local variables and parameters
        - provided the basePtr has been initialized properly

    - Just before returning
        - a subrouting stores its return value in the location labeled Return Value
        - bc the return value always resides at the bottom of the activation record
            - the calling subroutine knows exactly where to find it

When subrouting finishes executing, the PVM performs:
1. Reestablishes the settings needed by the calling subrouting by  
    - restoring the values of the location counter and the basePtr from values stored in the activation record

2. Pops the activatino record from the call stack

3. Resumes execution of the calling subrouting at the locatino indicated by the location counter
        

example:
    def factorial(n):
        if n == 1:
            return 1
        else:
            return n * factorial(n-1)

    factorial(4)


    # call stack needed to execute factorial(4)

    n              [1]  Activation record for
    return value   [ ]      factorial(1)
                     ^
    n              [2]  Activation record for
    return value   [ ]      factorial(2)
                     ^
    n              [3]  Activation record for
    return value   [ ]      factorial(3)
                     ^
    n              [4]  Activation record for
    return value   [ ]      factorial(4)

note:
    - each activatino record on the stack includes cells for the argument and return value of a particular function call
        - before each call returns, its value is placed in the empty cell so that the caller can access it
        
## The stack resource in the collection hierarchy


                AbstractColletion  
                        ^
                        |
                 AbstractStack
                        ^
               _________|________
               |                |
               | StackInterface |
            LinkedStack      ArrayStack


ArrayStack and LinkedStack
* Inherit from AbstractionStack
    - Add
* Inherit from AbstractCollection
    - is_empty
    - __len__
    - __str__
    - __add__
    - __eq__

* Implement in each
    - __init__
    - peek
    - push
    - pop
    - clear
    - __iter__

## Linked Stack
Pushing an item onto a linked stack
Steps:
1. set new_node to Node(d, self.items)

self.items
   |
   v
+---+    +------+    +------+    +------+
|  -|--> | a | -|->  | b | -|->  | c | \| 
+---+    +------+    +------+    +------+
             ^
             |
        +-------+
        | d |   |
        +-------+
          ^
          |
        newNode


2: set self.items to newNode

self.items
   |
   v
+---+    +------+    +------+    +------+
| | |    | a | -|->  | b | -|->  | c | \| 
+---+    +------+    +------+    +------+
  |          ^
  |          |
  |     +-------+
  ┗---> | d |   |
        +-------+
          ^
          |
        newNode



Popping an item from a linked stack

set self.items to self.items.next

self.items
   |
   v
+---+    +------+    +------+    +------+
| | |    | a | -|->  | b | -|->  | c | \| 
+---+    +------+    +------+    +------+
  |                    ^
  |                    |
  ┗--------------------┘



Issue:
    - Linked structure supports simple push/pop 
        - The __iter__ mmethod is complicated by fact the items must be visited from tail of linked structure to its head
        - but to traverse a singly linked structure you must begin at its head and follow the next links to its tail

    - recursion can be used within _-iter__ method
        * create temporary list and define a recusrive helper function that expects a node as an arg
            - use this to advance toward the tail of the structure
            - when call returns, you append t he node's data to the temporary list
                - when top-level call of the helper function returns, you return an iterator on the list


## Runtime
- All stack methods are simple and have max run time of O(1)
    * Except __iter__ method

Array Implementation
    * at moment of doubling, push method's running time jumps to O(n)
        - rest remain O(1)
        - same for pop
        - on average both still O(1)


__iter__ method
* Linear time in both implementations
    - but recursive in linked causes linear growth of memory bc use of system call stack
        - can use doubly linked structure to avoid this, but that uses more memory