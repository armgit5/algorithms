# https://leetcode.com/problems/critical-connections-in-a-network/
# https://www.geeksforgeeks.org/bridge-in-a-graph/
# https://leetcode.com/problems/critical-connections-in-a-network/discuss/1334523/C%2B%2B-Tarjan-Algo-Short-and-Clear-O(V%2BE)

from typing import List
from collections import defaultdict

# 1. compare lower values of current node and edges not parent -> assign edge disc to current low
# 2. compare low current with disc of parent -> low > disc is bridge

class Solution:
    def __init__(self):
        self.graph = defaultdict(list)
        self.time = 1
        self.bridges = []


    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        # create graph
        for c in connections:
            self.graph[c[0]].append(c[1])
            self.graph[c[1]].append(c[0])
        # print(self.graph)

        low = [-1] * n
        disc = [-1] * n

        def dfs(u, parent):
            disc[u] = self.time
            low[u] = self.time
            self.time += 1

            # search edges
            for v in self.graph[u]:
                if disc[v] == -1: # not visited
                    dfs(v, u)
                    # 1 compare lows
                    low[u] = min(low[v], low[u])
                    # 2 check low > disc?
                    if low[v] > disc[u]:
                        self.bridges.append((u,v))
                elif v != parent: # check edge is not parent
                    low[u] = min(low[v], low[u])


        dfs(0, 0)
        return self.bridges


s = Solution()
n = 4
connections = [[0, 1], [1, 2], [2, 0], [1, 3]]
print(s.criticalConnections(n, connections))

s = Solution()
n = 5
connections = [[1, 2], [1, 0], [0, 2], [0, 3], [3, 4]]
print(s.criticalConnections(n, connections))