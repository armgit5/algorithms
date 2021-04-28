# https://www.geeksforgeeks.org/snake-ladder-problem-2/
# https://www.youtube.com/watch?v=1pMNYQmtVVg
# https://www.hackerrank.com/challenges/the-quickest-way-up/problem

# ladders = [[32, 62], [42, 68], [12, 98]]
# snakes = [[95, 13], [97, 25], [93, 37], [79, 27], [75, 19], [49, 47], [67, 17]]
# ladders2 = [[8, 52], [6, 80], [26, 42], [2, 72]]
# snakes2 = [[51, 19], [39, 11], [37, 29], [81, 3], [59, 5], [79, 23], [53, 7], [43, 33], [77, 21]]


def input():
    return next(f)

def quickestWayUp(ladders, snakes):
    move = {} # store ladder or snake down
    visited = [0] * 101

    for l in ladders:
        move[l[0]] = l[1]

    for s in snakes:
        move[s[0]] = s[1]

    # Use breath first search to go up
    q = [(1,0)] # queue of node (point, distance)

    while len(q) > 0:
        node = q.pop(0)
        position = node[0]
        distance = node[1]

        # check if it's the end
        if position == 100:
            return distance

        # toss the dice
        for i in range(1, 7):
            newPos = position + i
            if newPos <= 100 and visited[newPos] == 0: # not visited
                if newPos in move:
                    newPos = move[newPos]
                visited[newPos] = 1
                newNode = (newPos, distance + 1)
                q.append(newNode)

    return -1

# ladders = [[7, 98]]
# snakes =  [[99, 1]]
#
# dist = quickestWayUp(ladders, snakes)
# print(dist)

with open('quickestWayUp2.txt') as f:
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        ladders = []

        for _ in range(n):
            ladders.append(list(map(int, input().rstrip().split())))

        m = int(input())

        snakes = []

        for _ in range(m):
            snakes.append(list(map(int, input().rstrip().split())))

        # print(ladders, snakes)
        dist = quickestWayUp(ladders, snakes)
        print(dist)