"""
File: algorithms.py
Project 12.4

Complete the function shortestPaths.

Graph processing algorithms
"""

from linkedstack import LinkedStack
from grid import Grid

INFINITY = "-"

def shortestPaths(g, startLabel):
    results = Grid(len(g), 3)
    included = []
    startVertex = g.getVertex(startLabel)
    
    initializeShortestPaths(results, included, g, startVertex)

    computeShortestPaths(results, included, g, startVertex)

    return results


def initializeShortestPaths(results, included, g, startVertex):
    row = 0
    for v in g.getVertices():
        results[row][0] = v
        if v == startVertex:
            results[row][1] = 0
            included.append(True)
        elif g.containsEdge(startVertex.getLabel(),
                            v.getLabel()):
            edge = g.getEdge(startVertex.getLabel(),
                             v.getLabel())
            results[row][1] = edge.getWeight()
            results[row][2] = startVertex
            included.append(False)
        else:
            results[row][1] = INFINITY
            results[row][2] = None
            included.append(False)
        row += 1

def computeShortestPaths(results, included,
                         g, startVertex):
    while True:   
        minDistIndex = findVertWithMinDist(results,
                                           included)
        if minDistIndex == -1:
            break
        included[minDistIndex] = True
        for row in range(g.sizeVertices()):
            if not included[row]:
                fromVert = results[minDistIndex][0]
                toVert = results[row][0]
                if g.containsEdge(fromVert.getLabel(),
                                  toVert.getLabel()):
                    edge = g.getEdge(fromVert.getLabel(),
                                     toVert.getLabel())
                    sumDist = addWithInfinity(results[minDistIndex][1],
                              edge.getWeight())
                    if isLessWithInfinity(sumDist, results[row][1]):
                        results[row][1] = sumDist
                        results[row][2] = fromVert
   
def findVertWithMinDist(results, included):
    minIndex = -1
    minDist = INFINITY
    for row in range(results.getHeight()):
        if not included[row]:
            dist = results[row][1]
            if isLessWithInfinity(dist, minDist):
                minDist = dist
                minIndex = row
    return minIndex

def topoSort(g, startLabel = None):  
    stack = LinkedStack()
    g.clearVertexMarks()
    for v in g.getVertices():
        if not v.isMarked():
            dfs(g, v, stack)
    return stack

def dfs(g, v, stack):
    v.setMark()
    for w in g.neighboringVertices(v.getLabel()):
        if not w.isMarked():
            dfs(g, w, stack)
    stack.push(v)

def spanTree(g, startLabel):
    # Exercise
    return ["Under development"]
	

def addWithInfinity(a, b):
    if a==INFINITY or b==INFINITY:
        return INFINITY
    else:
        return a+b

def isLessWithInfinity(a,b):
    if b==INFINITY:
        return True
    elif a == INFINITY:
        return False
    return a < b