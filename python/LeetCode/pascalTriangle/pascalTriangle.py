
# https://leetcode.com/problems/pascals-triangle/

class Solution:
    def generate(self, numRows: int):
        triangle = []

        for row in range(numRows):
            # create empty array for a row
            rowArr = [None for _ in range(row + 1)]
            # first and last row is 1
            rowArr[0], rowArr[-1] = 1, 1

            # if rn >= 2, sum the middles
            for col in range(1, row):
                rowArr[col] = triangle[row-1][col-1] + triangle[row-1][col]

            triangle.append(rowArr)
        return triangle



s = Solution()

numRows = 5
print(s.generate(numRows))
assert s.generate(numRows) == [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]

numRows = 1
print(s.generate(numRows))
assert s.generate(numRows) == [[1]]