from .graph import Graph

def topologicalSort(graph):
    inDegrees = {}
    zeroDegreeList = []
    nodes = graph.nodeList

    for i in range(len(nodes)):
        temp = nodes[i]
        temp = temp.__next__

        while temp:
            count = 0 if temp.id not in inDegrees else inDegrees[temp.id]
            inDegrees[temp.id] = count+1
            temp = temp.__next__

    for i in range(len(nodes)):
        temp = nodes[i]

        if temp.id not in inDegrees:
            zeroDegreeList.append(temp)


    while len(zeroDegreeList) != 0:
        curr = zeroDegreeList.pop(0)
        print(curr.id)
        temp = curr.__next__

        while temp:
            prevInDegree = inDegrees[temp.id]
            inDegrees[temp.id] = prevInDegree-1
            if prevInDegree == 1:
                zeroDegreeList.append(graph.getNode(temp.id))
            temp = temp.__next__


graph = Graph()
graph.addEdge(3,4)
graph.addEdge(3,1)

graph.addEdge(1,6)
graph.addEdge(1,2)
graph.addEdge(1,4)



graph.addEdge(4,2)
graph.addEdge(4,5)
graph.addEdge(6,5)
# graph.printGraph()

topologicalSort(graph)