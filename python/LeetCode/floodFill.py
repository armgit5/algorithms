# https://leetcode.com/problems/flood-fill/
from typing import List
class Solution:



    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        color = image[sr][sc]
        R = len(image)
        C = len(image[0])
        if newColor == color: return image

        def validRange(r, c):
            return r >= R or r < 0 or c >= C or c < 0

        def dfs(r, c):

            if validRange(r, c) or image[r][c] != color or image[r][c] == newColor:
                return

            image[r][c] = newColor
            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c+1)
            dfs(r, c-1)

        dfs(sr, sc)
        return image




s = Solution()
image = [[1,1,1],[1,1,0],[1,0,1]]
sr = 1
sc = 1
newColor = 2
print(s.floodFill(image, sr, sc, newColor))


image = [[0,0,0],[0,0,0]]
sr = 0
sc = 0
newColor = 2
print(s.floodFill(image, sr, sc, newColor))