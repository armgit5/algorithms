# https://leetcode.com/problems/island-perimeter/
# https://leetcode.com/problems/island-perimeter/discuss/1333293/Python-solution-using-2-approaches-with-explanation

from typing import List
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:

        count = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):

                if grid[i][j] == 1:
                    count += 4

                    # Check if grid before is island
                    # if so subtract both perimeters of 2 adj islands by 2
                    if i > 0 and grid[i-1][j] == 1: count -= 2
                    if j > 0 and grid[i][j-1] == 1: count -= 2

        return count

grid = [[0, 1, 0, 0], [1, 1, 1, 0], [0, 1, 0, 0], [1, 1, 0, 0]]
# grid = [[1]]
s = Solution()
print(s.islandPerimeter(grid))