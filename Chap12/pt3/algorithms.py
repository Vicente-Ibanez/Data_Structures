"""
File: algorithms.py
Project 12.3

Completes the function spanTree.

Graph processing algorithms
"""

from linkedstack import LinkedStack
from grid import Grid

INFINITY = "-"

def topoSort(g, startLabel = None):  
    stack = LinkedStack()
    g.clearVertexMarks()
    for v in g.getVertices():
        if not v.isMarked():
            dfs(g, v, stack)
    lyst = []
    return stack

def dfs(g, v, stack):
    v.setMark()
    for w in g.neighboringVertices(v.getLabel()):
        if not w.isMarked():
            dfs(g, w, stack)
    stack.push(v)

def spanTree(g, startLabel):
    g.clearVertexMarks()
    g.clearEdgeMarks()
    startVertex = g.getVertex(startLabel)
    startVertex.setMark()

    stack = LinkedStack()
    spEdges = []

    # Push start vertex incident edges in reverse so the first neighbor
    # is processed first (stack is LIFO). Use list slicing [::-1] instead of reversed().
    for v in list(startVertex.neighboringVertices())[::-1]:
        stack.push(startVertex.getEdgeTo(v))

    while len(spEdges)< g.sizeVertices() - 1 and not stack.isEmpty():
        edge = stack.pop()
        v = edge.getToVertex()

        if not v.isMarked():
            v.setMark()
            edge.setMark()
            spEdges.append(edge)

            # Push neighbors in reverse order for deterministic left-to-right visit
            # Use list slicing [::-1] instead of reversed().
            for w in list(v.neighboringVertices())[::-1]:
                if not w.isMarked():
                    stack.push(v.getEdgeTo(w))

    # print('p>s:0 p>q:0 s>t:0 q>r:0')
    # print('s>d:0 d>f:0')
    return spEdges

def findLeastCostEdge(visitedVertices, g):
    def findLeastCost(v, g):
        resultEdge = None
        minWeight = INFINITY
        for edge in g.incidentEdges(v.getLabel()):
            toVertex = edge.getToVertex()
            if not toVertex.isMarked() and \
               isLessWithInfinity(edge.getWeight(), minWeight):
                minWeight = edge.getWeight()
                resultEdge = edge
        return resultEdge
    leastCostEdge = None
    for v in visitedVertices:
        leastCostEdge = findLeastCost(v, g)
        if leastCostEdge != None:
            return leastCostEdge
    return leastCostEdge

def shortestPaths(g, startLabel):
    # Exercise
    return ["Under development"]

def isLessWithInfinity(a, b):
    """Returns True if a < b, or False otherwise.
    a and/or b might be INFINITY."""
    if a == INFINITY and b == INFINITY: return False
    elif b == INFINITY: return True
    elif a == INFINITY: return False
    else: return a < b


