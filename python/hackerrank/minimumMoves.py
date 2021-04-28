# https://www.hackerrank.com/challenges/castle-on-the-grid/problem

# ['.X.', '.X.', '...'] 0 0 0 2
# ['...', '.X.', '.X.'] 2 0 0 2

def isValid(grid, x, y):
    return x >= 0 and x < len(grid[0]) and y >= 0 and y < len(grid) and grid[x][y] == '.'

def minimumMoves(grid, startX, startY, goalX, goalY):
    q = [(startX, startY, 0)]
    visited = {(startX, startY)}
    moves = ((1, 0), (-1, 0), (0, 1), (0, -1))

    while len(q) > 0:
        p = q.pop(0)
        x, y, cnt = p[0], p[1], p[2]

        # iterate all directions
        for m in moves:
            nx, ny = x, y
            while True:
                nx, ny = nx + m[0], ny + m[1]
                if isValid(grid, nx, ny):
                    if (nx, ny) == (goalX, goalY):
                        return cnt + 1
                    else:
                        if (nx, ny) not in visited:
                            visited.add((nx, ny))
                            q.append((nx, ny, cnt + 1))
                else:
                    break

    return -1

# grid = ['.X.', '.X.', '...']
# m = minimumMoves(grid, 0, 0, 0, 2)
# print(m)
#
# m = minimumMoves(['...', '.X.', '.X.'], 2, 0, 0, 2)
# print(m)

# minimumMoves2 ans = 16 but it's slow at the moment
with open('minimumMoves2.txt') as f:
    n = int(next(f))

    grid = []

    for _ in range(n):
        grid_item = next(f).rstrip()
        grid.append(grid_item)

    startXStartY = next(f).split()

    startX = int(startXStartY[0])

    startY = int(startXStartY[1])

    goalX = int(startXStartY[2])

    goalY = int(startXStartY[3])

    # print(grid, startX, startY, goalX, goalY)

    result = minimumMoves(grid, startX, startY, goalX, goalY)
    print(result)

# start = 0
# end = 5000
# step = 100
#
# for i in range(start, end + 1, step):
#     print(i)


a = {(1,3), (2,4)}
print(a)
a.add((1,2))
a.add((1,3))
print(a)
print(type(a))