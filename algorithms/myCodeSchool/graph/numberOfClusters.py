matrix = [[1,0,1,0,1],
          [1,1,0,0,0],
          [0,1,0,1,1]]

class NumOfCusters():

    def __init__(self):
        self.offsets = [-1,0,1]

    def neighborExists(self, matrix, i, j):
        if i >= 0 and i < len(matrix) and j >= 0 and j < len(matrix[0]):
            if matrix[i][j] == 1:
                return True

    def doDFS(self, matrix, i, j, visited):
        if visited[i][j]:
            return None
        visited[i][j] = True

        for l in range(len(self.offsets)):
            xOffset = self.offsets[l]
            for m in range(len(self.offsets)):
                yOffset = self.offsets[m]

                if xOffset == 0 and yOffset == 0:
                    continue

                if self.neighborExists(matrix, i + xOffset, j + yOffset):
                    self.doDFS(matrix, i + xOffset, j + yOffset, visited)



    def findNumberOfClsters(self, matrix):
        visited = [[False] * len(matrix[0]) for i in range(len(matrix))]

        count = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] and visited[i][j] == False:
                    count += 1
                    self.doDFS(matrix, i, j, visited)

        return count

cluster = NumOfCusters()
print cluster.findNumberOfClsters(matrix)