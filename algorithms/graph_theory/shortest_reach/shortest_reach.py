def raw_input():
    return next(f)

class Graph(object):
    def __init__(self, nodes=None, edges=None):
        self.nodes = {}

    def _clear_visited(self):
        for node in self.nodes:
            node.visited = False

    def insert_node(self, node_from, node_to):
        if node_from not in self.nodes:
            self.nodes[node_from] = [node_to]
        else:
            self.nodes[node_from].extend([node_to])

    def bfs(self, start_node, visited_list):

        distances = {start_node: 0}

        queue = [start_node]
        visited_list[start_node] = True


        while queue:
            node = queue.pop(0)
            distance = distances[node] + 6
            out_edges = []
            if node in self.nodes:
                out_edges = self.nodes[node]
            for e in out_edges:
                if visited_list[e] == False:
                    queue.append(e)
                    visited_list[e] = True
                    distances[e] = distance

        return distances

def print_distances(s, n, distances):
    output = ""
    for i in range(1, n + 1):
        if (i == s):
            continue
        if i in distances:
            output += str(distances[i]) + " "
        else:
            output += "-1 "
    return output


with open('shortest_reach2.txt') as f:
    q = map(int, raw_input().split())[0]

    for q in xrange(q):
        n, m = raw_input().strip().split(' ')
        n, m = [int(n), int(m)]

        graph = Graph()

        for _ in xrange(m):
            node_from, node_to = raw_input().strip().split(' ')
            node_from, node_to = [int(node_from), int(node_to)]
            graph.insert_node(node_from, node_to)
            graph.insert_node(node_to, node_from)

        s = map(int, raw_input().split())[0]

        visited_list = [False] * (n + 1)

        distances = graph.bfs(s,visited_list)
        print print_distances(s, n, distances)




