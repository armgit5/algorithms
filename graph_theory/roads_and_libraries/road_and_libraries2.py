def raw_input():
    return next(f)

class Graph(object):
    def __init__(self, nodes=None, edges=None):
        self.nodes = {}
        self.count = 1

    def _clear_visited(self):
        for node in self.nodes:
            node.visited = False

    def insert_node(self, node_to, node_from):
        if node_to not in self.nodes:
            self.nodes[node_to] = [node_from]
        else:
            self.nodes[node_to].extend([node_from])

    def dfs(self, start_node, visited_list):
        visited_list[start_node] = True

        for n in self.nodes[start_node]:
            if visited_list[n] == False:
                self.count += 1
                self.dfs(n, visited_list)

with open('road_and_libraries3.txt') as f:

    q = int(input().strip())

    for a0 in range(q):

        graph = Graph()
        graph._clear_visited()

        n, m, x, y = input().strip().split(' ')
        n, m, x, y = [int(n), int(m), int(x), int(y)]
        for a1 in range(m):
            city_1, city_2 = input().strip().split(' ')
            city_1, city_2 = [int(city_1), int(city_2)]

            graph.insert_node(city_1, city_2)
            graph.insert_node(city_2, city_1)

        total_cost = 0
        visited_list = [False] * (n + 1)


        for i in range(1, n+1):

            if visited_list[i] == False:
                graph.count = 1
                if i in graph.nodes:
                    graph.dfs(i, visited_list)

                total_cost += x

                if x > y:
                    total_cost += (graph.count - 1) * y
                else:
                    total_cost += (graph.count - 1) * x

        print(total_cost)


