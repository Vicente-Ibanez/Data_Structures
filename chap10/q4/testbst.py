"""
File: testbst.py

A tester program for binary search trees.
"""

from linkedbst import LinkedBST

def main():
    tree = LinkedBST()
    print("Adding D B A C F E G")
    tree.add("D")
    tree.add("B")
    tree.add("A")
    tree.add("C")
    tree.add("F")
    tree.add("E")
    tree.add("G")
    print("\nString:\n" + str(tree))
    
    for item in tree:
        print("Predecessor of " + item + ": ", tree.predecessor(item))
        print("Successor of " + item + ": ", tree.successor(item))
    
    item = "Q"
    print("Predecessor of " + item + ": ", tree.predecessor(item))
    print("Successor of " + item + ": ", tree.successor(item))



if __name__ == "__main__":
    main()
