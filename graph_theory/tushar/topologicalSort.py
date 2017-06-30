from .graph import Graph

def topSortUtil(node, stack, visited):
    visited.append(node)
    for neighbor in node.adjacentNodes:
        if neighbor in visited:
            continue
        topSortUtil(neighbor, stack, visited)
    stack.append(node.id)


def topSort(graph):
    stack = []
    visited = []
    for id, node in graph.allNodes.items():
        if node in visited:
            continue
        topSortUtil(node, stack, visited)
    stack.reverse()
    return stack


graph = Graph(True)
graph.addEdge("A","C")
graph.addEdge("B","C")
graph.addEdge("B","E")
graph.addEdge("C","D")
graph.addEdge("D","F")
graph.addEdge("E","F")
graph.addEdge("F","G")

print(topSort(graph))