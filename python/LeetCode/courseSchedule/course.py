# https://leetcode.com/problems/course-schedule-iv/
# https://leetcode.com/problems/course-schedule-iv/discuss/1253423/DFS-%2B-memo-O(n3)-solution-in-python
# https://leetcode.com/problems/course-schedule-iv/discuss/1277752/Three-python-solution
from typing import List
from collections import defaultdict

class Solution:

    def makeGraph(self, prereqs):
        d = defaultdict(list)
        for i, j in prereqs:
            d[j].append(i)
        return d

    def checkHelper(self, i, j):
        q = [j]
        visited = set([j])


        while q:
            node = q.pop(0)
            # visited.add(node) # 4984ms
            if i == node:
                return True
            for adj in self.graph[node]:
                if adj not in visited:
                    q.append(adj)
                    visited.add(adj) # 2596ms
        return False

    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[
        bool]:
        self.graph = self.makeGraph(prerequisites)
        print('graph', self.graph)
        return [self.checkHelper(i, j) for i, j in queries]


# d = defaultdict(list)
# d['a'].append('b')
# print(d)


# numCourses = 2
# prerequisites = [[1,0]]
# queries = [[0,1],[1,0]]

# numCourses = 2
# prerequisites = []
# queries = [[1,0],[0,1]]


numCourses = 3
prerequisites = [[1,2],[1,0],[2,0]]
queries = [[1,0],[1,2]]

s = Solution()
l = s.checkIfPrerequisite(numCourses, prerequisites, queries)
print(l)
