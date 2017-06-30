# https://www.youtube.com/watch?annotation_id=annotation_2195265949&feature=iv&src_vid=Y0ZqKpToTic&v=NJuKJ8sasGk

import sys

total = 6
coins = [3,2,4]

def minCoinBottomUp(total, coins):
    T = [sys.maxsize for _ in range(total+1)]
    R = [-1 for _ in range(total+1)]

    T[0] = 0

    for j in range(len(coins)):
        for i in range(total+1):
            if i >= coins[j]:
                if T[i-coins[j]] + 1 < T[i]:
                    T[i] = T[i-coins[j]] + 1
                    R[i] = j
    printCoinCombination(R, coins)
    return T[total]

def printCoinCombination(R, coins):
    if R[len(R)-1] == -1:
        print("No solution possible")
        return
    start = len(R)-1
    print("Coins used")
    while start != 0:
        j = R[start]
        print((coins[j]))
        start -= coins[j]
    print("")

print((minCoinBottomUp(total, coins)))