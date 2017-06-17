from graph import Graph
from disjointSet import DisjointSet

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


graph = Graph()
graph.addEdge("A","D",1)
graph.addEdge("A","B",3)
graph.addEdge("B","C",1)
graph.addEdge("B","D",3)
graph.addEdge("C","D",1)
graph.addEdge("C","F",4)
graph.addEdge("C","E",5)
graph.addEdge("D","E",6)
graph.addEdge("E","F",2)

result = getMST(graph)
for e in result:
    print e.node1.id, e.node2.id, e.weight

