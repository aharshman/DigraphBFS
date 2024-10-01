# -*- coding: utf-8 -*-
"""
Created on Thu Feb 17 12:01:47 2022

@author: Alexa
"""

from digraph import *

def BFS(graph, start, end, toPrint=False):
    """Assume graph is a digraph"""
    
    initPath = [start]
    pathQueue = [initPath]
    
    if toPrint:
        print('Current Path is:', printpath(initPath))
        
    while len(pathQueue) != 0:
        tmpPath = pathQueue.pop(0)  # Removes and Returns index 0 in pathQueue
        print('Current Path is:', printpath(tmpPath))
        lastnode = tmpPath[-1]
        
        if lastnode == end:
            return tmpPath
    
        for nextNode in graph.children_of(lastnode):  # Pass the last node to get children
            if nextNode not in tmpPath:
                newPath = tmpPath + [nextNode]
                pathQueue.append(newPath)  # Fixed typo here
    
    return None
                
                
def printpath(path):
    """Assumes path is a list of nodes"""
    
    result = ' '
    for i in range(len(path)):
        result += str(path[i]) + ' ---> '
    return result[:-6]  # Remove last arrow and space


def testBFS():
    
    nodes = []

    for name in range(6):  # Create 6 nodes
        nodes.append(Node(str(name)))

    g = Digraph()

    for n in nodes:
        g.add_node(n)

    g.add_edge(Edge(nodes[0], nodes[1]))
    g.add_edge(Edge(nodes[1], nodes[2]))
    g.add_edge(Edge(nodes[2], nodes[3]))
    g.add_edge(Edge(nodes[2], nodes[4]))
    g.add_edge(Edge(nodes[3], nodes[4]))
    g.add_edge(Edge(nodes[3], nodes[5]))
    g.add_edge(Edge(nodes[4], nodes[1]))
    g.add_edge(Edge(nodes[0], nodes[4]))
    g.add_edge(Edge(nodes[0], nodes[2]))
    g.add_edge(Edge(nodes[1], nodes[0]))
    g.add_edge(Edge(nodes[3], nodes[1]))
    g.add_edge(Edge(nodes[4], nodes[0]))
    
    sp = BFS(g, nodes[0], nodes[5], True)
    print('\nBFS shortest path is:', printpath(sp))
    
testBFS()
