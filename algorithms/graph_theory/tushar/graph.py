class Node():
    def __init__(self, id, data=None):
        self.id = id
        self.data = data
        self.edges = []
        self.adjacentNodes = []

    def addAdjacentNode(self, edge, node):
        self.edges.append(edge)
        self.adjacentNodes.append(node)

class Edge():
    def __init__(self, node1, node2, weight=0, isDirected=False):
        self.isDirected = False
        self.node1 = node1
        self.node2 = node2
        self.weight = weight

class Graph():
    def __init__(self, isDirected=False):
        self.allEdges = []
        self.allNodes = {}
        self.isDirected = isDirected

    def addEdge(self, id1, id2, weight=0):
        node1, node2 = None, None
        if id1 in self.allNodes:
            node1 = self.allNodes[id1]
        else:
            node1 = Node(id1)
            self.allNodes[id1] = node1
        if id2 in self.allNodes:
            node2 = self.allNodes[id2]
        else:
            node2 = Node(id2)
            self.allNodes[id2] = node2

        edge = Edge(node1, node2, weight)
        self.allEdges.append(edge)
        node1.addAdjacentNode(edge, node2)

        if self.isDirected == False:
            node2.addAdjacentNode(edge, node1)

    def setDataForNode(self, id, data):
        if id in self.allNodes:
            node = self.allNodes[id]
            node.data = data

    def toString(self):
        for edge in self.allEdges:
            print edge.node1, edge.node2, edge.weight

