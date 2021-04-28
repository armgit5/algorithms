# https://www.hackerrank.com/challenges/ctci-bfs-shortest-reach/problem

# nm = [[4, 2], [3, 1]]
# s = [1, 2] # starting node num
# xy = [[[1, 2], [1, 3]], [[2, 3]]]
# t = 2

nm = [[6, 4]]
s = [1] # starting node num
xy = [[[1, 2], [2, 3], [3, 4], [1, 5]]]
t = 1

import sys
class Graph():
    def __init__(self, n):
        self.nodes = {}
        self.distances = [-1] * (n)
        self.visited = []
        for i in range(1, n + 1):
            self.nodes[i] = []

    def connect(self, u, v):
        self.nodes[u].append(v)
        self.nodes[v].append(u)

    def find_all_distances(self, s):
        # Start breath first search
        Q = []
        Q.append(s)
        self.distances[s - 1] = 0
        while len(Q) > 0:
            current = Q.pop(0)
            self.visited.append(current)
            # loop edges
            for e in self.nodes[current]:
                if e not in self.visited:
                    self.distances[e - 1] = self.distances[current - 1] + 6
                    self.visited.append(e)
                    Q.append(e)

        self.distances.pop(s - 1)
        print(' '.join(map(str, self.distances)))

# {1: [2, 5], 2: [1, 3], 3: [2, 4], 4: [3], 5: [1], 6: []}

for i in range(t):
    n,m = nm[i]
    # print('nm ', n, m)

    graph = Graph(n)

    for j in range(m):
        x,y = xy[i][j]
        graph.connect(x, y)
    print(graph.nodes)

    # print('s ', s[i])
    graph.find_all_distances(s[i])
    graph.distances.pop(s[i] - 1)
    # print(graph.distances)
