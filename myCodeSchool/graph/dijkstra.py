import sys

class Node():

    def __init__(self, id=None, dist=0):
        self.id = id
        self.next = None
        self.parentDist = dist

class Graph():

    def __init__(self):
        self.nodeList = []

    def addNode(self, id):
        node = Node(id)
        self.nodeList.append(node)

    def addEdge(self, id1, id2, dist):

        for i in range(len(self.nodeList)):
            if self.nodeList[i].id == id1:
                node1 = self.nodeList[i]
                node2 = Node(id2, dist)

                node2.next = node1.__next__
                node1.next = node2

                break

    def printGraph(self):
        for i in range(len(self.nodeList)):
            curr = self.nodeList[i]

            while curr != None:
                print(curr.id, curr.parentDist)
                curr = curr.__next__

            print("")

    def findShortest_Dijkstra(self, start):

        dist = [sys.maxsize] * len(self.nodeList)
        prev = [-1] * len(self.nodeList)
        visited = [False] * len(self.nodeList)

        dist[start] = 0
        Q = [self.nodeList[start]]

        while len(Q) != 0:
            currNode = Q.pop(0)
            visited[currNode.id] = True
            neighborNode = currNode.__next__ if currNode.__next__ else None
            while neighborNode:
                if visited[neighborNode.id] == False:
                    alt = dist[currNode.id] + neighborNode.parentDist
                    if alt < dist[neighborNode.id]:
                        dist[neighborNode.id] = alt
                        prev[neighborNode.id] = currNode.id
                        dist[neighborNode.id] = alt
                        Q.append(self.nodeList[neighborNode.id])
                neighborNode = neighborNode.__next__

        print(dist, prev)

graph = Graph()

graph.addNode(0)
graph.addNode(1)
graph.addNode(2)
graph.addNode(3)
graph.addNode(4)
graph.addNode(5)
graph.addNode(6)

graph.addEdge(0,1,3)
graph.addEdge(0,2,4)
graph.addEdge(1,3,4)
graph.addEdge(1,4,6)
graph.addEdge(2,4,6)
graph.addEdge(3,5,5)
graph.addEdge(4,5,7)
graph.addEdge(4,6,5)

# graph.printGraph()
graph.findShortest_Dijkstra(0)

