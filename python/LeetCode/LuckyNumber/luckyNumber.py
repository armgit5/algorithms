# https://leetcode.com/problems/lucky-numbers-in-a-matrix/

class Solution(object):
    # Min row Max col
    def luckyNumbers(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        # print(matrix)

        minRow = {}
        maxCol = {}

        # Scan rowr
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                # Get min row
                if i in minRow:
                    if matrix[i][j] < matrix[i][minRow[i]]:
                        minRow[i] = j
                else:
                    minRow[i] = j

                # Get max col
                if j in maxCol:
                    if matrix[i][j] > matrix[maxCol[j]][j]:
                        maxCol[j] = i
                else:
                    maxCol[j] = i

        # print(minRow)
        # print(maxCol)

        # Check to find min row max col
        # min row col has to equal to max col row
        ret = []
        for rKey in minRow:
            rVal = minRow[rKey]
            if maxCol[rVal] == rKey:
                ret.append(matrix[rKey][rVal])
                # print(rKey, rVal)
                # print(matrix[rKey][rVal])
        return ret

# input = [[3,7,8],[9,11,13],[15,16,17]]
# input = [[1,10,4,2],[9,3,8,7],[15,16,17,12]]
input = [[7,8],[1,2]]
s = Solution()
print(s.luckyNumbers(input))