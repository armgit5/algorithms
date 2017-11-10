# https://www.youtube.com/watch?v=5dJSZLmDsxk&index=4&list=PLBZBJbE_rGRVnpitdvpdY9952IsKMDuev

matrix = [[-3,-2,-1,1],
          [-2,2,3,4],
          [4,5,7,8]]


def negativeNumInMatrix(M, n, m):
    count = 0
    i = 0
    j = m - 1
    while i < n and j >= 0:
        if M[i][j] < 0:
            count += j + 1
            i += 1
        else:
            j -= 1
    return count

num = negativeNumInMatrix(matrix, len(matrix), len(matrix[0]))
print(num)