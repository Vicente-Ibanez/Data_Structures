"""
File: testbst.py
Project 10.5

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
    
    print("Items in range C..E:", tree.rangeFind("C", "E"))



if __name__ == "__main__":
    main()
