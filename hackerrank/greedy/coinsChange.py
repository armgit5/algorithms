# https://www.hackerrank.com/challenges/coin-change
# https://www.youtube.com/watch?v=Y0ZqKpToTic&list=PLrmLmBdmIlpsHaNTPP_jHHDx_os9ItYXr&index=6

import sys
n,m,c = 4, 3, [1, 2, 3]

def getWays(total, coins):
    T = [[0 for _ in range(total+1)] for _ in range(len(coins)+1)]

    for i in range(len(coins)+1):
        T[i][0] = 1

    for i in range(1, len(coins)+1):
        for j in range(1, total+1):
            # take value from the top
            if coins[i-1] > j:
                T[i][j] = T[i-1][j]
            else:
                T[i][j] = T[i][j-coins[i-1]] + T[i-1][j]
    return T[len(coins)][total]

def getWayOnSpace(total, coins):
    T = [0 for _ in range(total+1)]

    T[0] = 1

    for i in range(len(coins)):
        for j in range(total+1):
            if j >= coins[i]:
                T[j] += T[j-coins[i]]
    return T[total]

def printCoinChangingSolution(total, coins):
    result = []
    printActualSolution(result, total, coins, 0)

def printActualSolution(result, total, coins, pos):
    if total == 0:
        for r in result:
            print r, " "
        print ""

    for i in range(pos, len(coins)):
        if total >= coins[i]:
            result.append(coins[i])
            printActualSolution(result, total-coins[i], coins, i)
            result.pop()

print getWays(n, c)
print getWayOnSpace(n, c)
print ""
printCoinChangingSolution(n, c)
