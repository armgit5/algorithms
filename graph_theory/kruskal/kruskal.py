# https://www.hackerrank.com/challenges/kruskalmstrsub
def raw_input():
    return next(f)

class DisjointSetNode():
    def __init__(self, data=None, rank=0):
        self.rank = rank
        self.parent = None
        self.data = data

class DisjointSet():

    def __init__(self):
        self.hashMap = {}

    def makeSet(self, data):
        node = DisjointSetNode(data)
        node.parent = node
        self.hashMap[data] = node

    def union(self, data1, data2):
        node1 = self.hashMap[data1]
        node2 = self.hashMap[data2]

        parent1 = self.findSetHelper(node1)
        parent2 = self.findSetHelper(node2)

        if parent1 == parent2:
            return
        if parent1.rank >= parent2.rank:
            parent1.rank = parent1.rank + 1 if parent1.rank == parent2.rank else parent1.rank
            parent2.parent = parent1
        else:
            parent1.parent = parent2

        return True

    def findSet(self, data):
        return self.findSetHelper(self.hashMap[data]).data

    def findSetHelper(self, node):
        if node == node.parent:
            return node

        node.parent = self.findSetHelper(node.parent)
        return node.parent

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

def getMST(graph):

    allEdges = graph.allEdges
    allEdges.sort(key=lambda x:x.weight)


    disjoinSet = DisjointSet()

    for k, node in graph.allNodes.iteritems():
        disjoinSet.makeSet(k)

    resultEdge = []

    for e in allEdges:
        root1 = disjoinSet.findSet(e.node1.id)
        root2 = disjoinSet.findSet(e.node2.id)

        if root1 == root2:
            continue
        else:
            resultEdge.append(e)
            disjoinSet.union(e.node1.id, e.node2.id)
    return resultEdge

with open('kruskal2.txt') as f:


    graph = Graph()

    n, m = raw_input().strip().split(' ')
    n, m = [int(n), int(m)]

    for i in xrange(m):
        id1, id2, weight = raw_input().strip().split(' ')
        id1, id2, weight = [int(id1), int(id2), int(weight)]

        graph.addEdge(id1, id2, weight)

    result = getMST(graph)
    total = 0
    for e in result:
        total += e.weight
    print total

