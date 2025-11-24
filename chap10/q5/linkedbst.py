"""
File: linkedbst.py
Project 10.5

Adds the method rangeFind to the tree.
"""

from abstractcollection import AbstractCollection
from bstnode import BSTNode
from math import log
from linkedstack import LinkedStack
from linkedqueue import LinkedQueue

class LinkedBST(AbstractCollection):
    """An link-based binary search tree implementation."""
	
	# Reuse your solution from Programming Exercise 10.4 as your starter file

    def __init__(self, sourceCollection = None):
        """Sets the initial state of self, which includes the
        contents of sourceCollection, if it's present."""
        self.root = None
        AbstractCollection.__init__(self, sourceCollection)
        
    # Accessor methods
    def __str__(self):
        """Returns a string representation with the tree rotated
        90 degrees counterclockwise."""
        def recurse(node, level):
            s = ""
            if node != None:
                s += recurse(node.right, level + 1)
                s += "| " * level
                s += str(node.data) + "\n"
                s += recurse(node.left, level + 1)
            return s
        return recurse(self.root, 0)

    def __iter__(self):
        """Supports a preorder traversal on a view of self."""
        if not self.isEmpty():
            stack = LinkedStack()
            stack.push(self.root)
            while not stack.isEmpty():
                node = stack.pop()
                yield node.data
                if node.right != None:
                    stack.push(node.right)
                if node.left != None:
                    stack.push(node.left)

    def __contains__(self, item):
        """Returns True if target is found or False otherwise."""
        return self.find(item) != None

    def find(self, item):
        """If item matches an item in self, returns the
        matched item, or None otherwise."""
        def recurse(node):
            if node is None:
                return None
            elif node.data == item:
                return node.data
            elif node.data > item:
                return recurse(node.left)
            else:
                return recurse(node.right)
        return recurse(self.root)

    # Mutator methods
    def clear(self):
        """Makes self become empty."""
        self.root = None
        self.size = 0

    def add(self, item):
        """Adds item to the tree."""

        # Helper function to search for item's position 
        def recurse(node):
            # New item is less, go left until spot is found
            if item < node.data:
                if node.left == None:
                    node.left = BSTNode(item)
                else:
                    recurse(node.left)
            # New item is greater or equal, 
            # go right until spot is found
            elif node.right == None:
                node.right = BSTNode(item)
            else:
                recurse(node.right)
            # End of recurse

        # Tree is empty, so new item goes at the root
        if self.isEmpty():
            self.root = BSTNode(item)
        # Otherwise, search for the item's spot
        else:
            recurse(self.root)
        self.size += 1

    def remove(self, item):
        """Precondition: item is in self.
        Raises: KeyError if item is not in self.
        postcondition: item is removed from self."""
        if not item in self:
            raise KeyError("Item not in tree.""")

        # Helper function to adjust placement of an item
        def liftMaxInLeftSubtreeToTop(top):
            # Replace top's datum with the maximum datum in the left subtree
            # Pre:  top has a left child
            # Post: the maximum node in top's left subtree
            #       has been removed
            # Post: top.data = maximum value in top's left subtree
            parent = top
            currentNode = top.left
            while not currentNode.right == None:
                parent = currentNode
                currentNode = currentNode.right
            top.data = currentNode.data
            if parent == top:
                top.left = currentNode.left
            else:
                parent.right = currentNode.left

        # Begin main part of the method
        if self.isEmpty(): return None
        
        # Attempt to locate the node containing the item
        itemRemoved = None
        preRoot = BSTNode(None)
        preRoot.left = self.root
        parent = preRoot
        direction = 'L'
        currentNode = self.root
        while not currentNode == None:
            if currentNode.data == item:
                itemRemoved = currentNode.data
                break
            parent = currentNode
            if currentNode.data > item:
                direction = 'L'
                currentNode = currentNode.left
            else:
                direction = 'R'
                currentNode = currentNode.right
                
        # Return None if the item is absent
        if itemRemoved == None: return None
        
        # The item is present, so remove its node

        # Case 1: The node has a left and a right child
        #         Replace the node's value with the maximum value in the
        #         left subtree
        #         Delete the maximium node in the left subtree
        if not currentNode.left == None \
           and not currentNode.right == None:
            liftMaxInLeftSubtreeToTop(currentNode)
        else:
            
        # Case 2: The node has no left child
            if currentNode.left == None:
                newChild = currentNode.right
                
        # Case 3: The node has no right child
            else:
                newChild = currentNode.left
                
        # Case 2 & 3: Tie the parent to the new child
            if direction == 'L':
                parent.left = newChild
            else:
                parent.right = newChild
            
        # All cases: Reset the root (if it hasn't changed no harm done)
        #            Decrement the collection's size counter
        #            Return the item
        self.size -= 1
        if self.isEmpty():
            self.root = None
        else:
            self.root = preRoot.left
        return itemRemoved

    def replace(self, item, newItem):
        """If item is in self, replaces it with newItem and
        returns the old item, or returns None otherwise."""
        probe = self.root
        while probe != None:
            if probe.data == item:
                oldData = probe.data
                probe.data = newItem
                return oldData
            elif probe.data > item:
                probe = probe.left
            else:
                probe = probe.right
        return None
    def preorder(self):
        """Supports a preorder traversal on a view of self."""
        visited = []

        def recurse(node, l):
            # append current node
            l.append(node.data)

            # go to left if possible
            if node.left != None:
                recurse(node.left, l)
            
            # then go right
            if node.right != None:
                recurse(node.right, l)
            
            return l
            
        return recurse(self.root, visited)
    

    def inorder(self):
        """Supports an inorder traversal on a view of self."""
        visited = []

        def recurse(node):
            if node is None:
                return
            recurse(node.left)
            visited.append(node.data)
            recurse(node.right)
        recurse(self.root)
        return visited
    
    
    def postorder(self):
        """Supports a postorder traversal on a view of self."""
        visited = []

        def recurse(node, l):

            if node.left != None:
                recurse(node.left, l)
            elif node.left == None:
                l.append(node.data)
                return l
            
            if node.right != None:
                recurse(node.right, l)
            elif node.right == None:
                l.append(node.data)
                return l
            
            l.append(node.data)


            return l
            
        return recurse(self.root, visited)

    def levelorder(self):
        """Supports a levelorder traversal on a view of self."""
        visited = []
        visited.append(self.root.data)
        def recurse(node, l):
            # l.append(node.data)

            if node.left!=None:
                l.append(node.left.data)
            if node.right!=None:
                l.append(node.right.data)

            if node.left!=None:
                recurse(node.left, l)
            if node.right!=None:
                recurse(node.right, l)

            

            return l
            
        return recurse(self.root, visited)

    
    def height(self):
        height = -1
        listHeights = []
        def recurse(node, l, h):
            h += 1
            if node.left != None:
                recurse(node.left, l, h)
            
            if node.right != None:
                recurse(node.right, l, h)

            if node.left == None and node.right == None:
                l.append(h)

            return l

        return max(recurse(self.root, listHeights, height))
    
    def isBalanced(self):
        return self.height() < 2 * log(len(self))
    
    def rebalance(self):
        items = self.inorder()
        if items == None:
            return
        ilen = len(items)

        def recurse(start, finish):
            if start > finish:
                return None
            
            mid = (start+finish) // 2
            node = BSTNode(items[mid])

            node.left = recurse(start, mid-1)
            node.right = recurse(mid+1, finish)

            return node
        self.root = recurse(0, ilen-1)
        
                
    def successor(self, item):

        def recurse(node):
            if node == None:
                return None
            
            # if node is bigger, check left for a node still bigger
            if node.data > item:
                if node.left:
                    r = recurse(node.left) 
                    # if left is not bigger (none returned), return self
                    if not r:
                        return node.data
                    return r
                else: # theres not other left, so return self as it is bigger
                    return node.data

            # if node is smaller, check the right side
            elif node.data <= item:
                 # if no right, then there's no node bigger than the item
                # and recurse will return none   
                if node.right:
                    return recurse(node.right)
                else:
                    return None 

        return recurse(self.root)
            
    def predecessor(self, item):
        def recurse(node):
            if node == None:
                return None
            
            # if node is less than item
            # check the right path for a larger node
            # that is still lower than item
            if node.data < item:
                if node.right:
                    r = recurse(node.right) 
                    # if there is a larger node
                    # that is lower then item
                    # then return that
                    # otherwise, return current node
                    if r:
                        return r
                        
                return node.data 
            # node is greater than or equal to item
            # check left branch for node that is 
            # less than item
            elif node.data >= item:
                if node.left:
                    return recurse(node.left)
                return None

        return recurse(self.root)
        
    def rangeFind(self, lower, upper):
        values = []
        def recurse(node):
            if node.data >= lower and node.data <= upper:
                values.append(node.data)
            
            if node.left and node.data >= lower:
                recurse(node.left)
            if node.right and node.data <= upper:
                recurse(node.right)
            return values
        
        return sorted(recurse(self.root))
