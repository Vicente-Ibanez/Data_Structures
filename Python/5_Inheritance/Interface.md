# Interface

* Python's help function shows information from the resources's interface
* Interface:
    - List of method headers, including names, types of their arguments, a statement of what the methods do, and the value they return
    - Gives enough information to know what the methods do and how to call them

Example: Bag Interface

    Operations          Method in Bag Class
    ----------          -------------------
    <class name>(collection)    __init__(self, source_collection=None)
    ^ constuctor

    add                 add(self, item)
    clear               clear(self)
    count               count(self, item)
    for                 __iter__(self)
    in                  __contains__(self, item)
    is_empty            isEmpty(self)
    len                 __len__(self)
    remove              remove(self, item)
    +                   __add__(self, other)
    ==                  __eq__(self, other)


Note
    * Interfaces in Python doesn't have feature to implemenet it. Can emulate it. 

Class diagram with an interface and two implementing classes


                  BagInterface
                      ^
              ________|________
              |               |
 Node --<> Linked Bag      Array Bag <>-- Array