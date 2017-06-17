from graph import Graph
from minimumHeap import BinaryMinHeap

def primMST(graph):

    maxV = 10000

    minHeap = BinaryMinHeap()
    nodeToEdge = {}
    result = []

    for n in graph.allNodes:
        minHeap.add(maxV, n)

    startNode = graph.allNodes["A"]
    minHeap.decrease(0, "A")

    while minHeap.empty() != True:
        current = minHeap.extractMinNode()
        # minHeap.printPositionMap()
        # print current
        if current in nodeToEdge:
            result.append(nodeToEdge[current])

        currentNode = graph.allNodes[current]
        for edge in currentNode.edges:
            adjacentNode = getNodeForEdge(currentNode, edge)

            # a = minHeap.contain(adjacentNode.id)
            # b = minHeap.getWeight(adjacentNode.id)
            # c = edge.weight
            # d = adjacentNode.id

            if minHeap.contain(adjacentNode.id) and edge.weight < minHeap.getWeight(adjacentNode.id):
                minHeap.decrease(edge.weight, adjacentNode.id)
                nodeToEdge[adjacentNode.id] = edge
    return result

def getNodeForEdge(n, e):
    return e.node2 if n == e.node1 else e.node1


graph = Graph()
graph.addEdge("A","D",1)
graph.addEdge("A","B",3)
graph.addEdge("B","D",3)
graph.addEdge("B","C",1)
graph.addEdge("C","D",1)
graph.addEdge("C","E",5)
graph.addEdge("C","F",4)
graph.addEdge("D","E",6)
graph.addEdge("E","F",2)

result = primMST(graph)

for e in result:
    print e.node1.id, e.node2.id, e.weight