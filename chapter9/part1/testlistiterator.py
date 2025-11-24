"""
File: testlistiterator.py

A tester program for list iterator implementation.
"""

from arraylist import ArrayList
from linkedlist import LinkedList
from arraysortedlist import ArraySortedList


def testListIterator(ListType):
    """Expects a list type as an argument and runs some tests
    on a list iterator on that type."""
    print("\nTESTING A LIST ITERATOR FOR THE TYPE " + str(ListType) )
    print("Create a list with 1-9")
    lyst = ListType(range(1, 10))
    print("Length:", len(lyst))
    print("Items in list (first to last):", lyst)
    
    # Create and use a list iterator
    listIterator = lyst.listIterator()
    print("Forward traversal with list iterator: ", end="")
    listIterator.first()
    while listIterator.hasNext(): 
            print(listIterator.next(), end = " ")

    print("\nBackward traversal: ", end="")
    listIterator.last()
    while listIterator.hasPrevious(): 
            print(listIterator.previous(), end=" ")

    print("\nInserting 10 before 3: ", end="")
    listIterator.first()
    for count in range(3):
            listIterator.next()
    listIterator.insert(10)
    print(lyst)
    print("Removing 2: ", end="")
    listIterator.first()
    for count in range(2): 
            listIterator.next()
    listIterator.remove()
    print(lyst)

    print("Replace all items with 0: ", end="")
    listIterator.first()
    while listIterator.hasNext():
            listIterator.next()
            listIterator.replace(0)
    print(lyst)

    print("Removing all items: Expect []: ", end = "")
    listIterator.first()
    while listIterator.hasNext():
            listIterator.next()
            listIterator.remove()
    print(lyst)
    print("Length:", len(lyst))
    
testListIterator(ArrayList)
#testListIterator(LinkedList)
testListIterator(ArraySortedList)
    
