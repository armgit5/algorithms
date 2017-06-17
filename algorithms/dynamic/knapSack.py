
val = [60, 120, 100]
wt = [10, 30, 20]
W = 50
n = len(val) - 1

def knapSack(W, wt, val, n):
    if n == 0 or W == 0:
        return 0

    if wt[n] > W:
        return knapSack(W, wt, val, n)
    else:
        return max(val[n] + knapSack(W-wt[n], wt, val, n-1), knapSack(W, wt, val, n-1))
'''
    if j < wt[i]:
        t[i][j] = T[i-1][j]
    else:
        T[i][j] = max(val[i] + T[i-1][j-wt[i]], T[i-1][j])
'''


def knapSackDy(W, wt, val):
    K = [[0 for _ in range(W+1)] for _ in range(len(val))]

    for i in range(len(val)):
        for j in range(1, W+1):
            if i == 0 or j == 0:
                K[i][j] = 0
                continue
            if j < wt[i]:
                K[i][j] = K[i-1][j]
            else:
                K[i][j] = max(val[i] + K[i-1][j-wt[i]], K[i-1][j])

    return K[n][W]


print knapSack(W, wt, val, n)
print knapSackDy(W, wt, val)

