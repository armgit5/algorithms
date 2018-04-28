# https://www.youtube.com/watch?v=Qf5R-uYQRPk&index=3&list=PLBZBJbE_rGRU5PrgZ9NBHJwcaZsNpf8yD

P = "BATD"
Q = "ABACD"
n = len(P)-1
m = len(Q)-1

result = 0
def LCS(P, Q, n, m, result):
    if n < 0 or m < 0:
        return 0
    if P[n] == Q[m]:
        result = 1 + LCS(P,Q,n-1,m-1,result)
    elif P[n] != Q[n]:
        tmp1 = LCS(P,Q,n-1,m,result)
        tmp2 = LCS(P,Q,n,m-1,result)
        result = max(tmp1, tmp2)
    return result

print(LCS(P,Q,n,m,result))



arr = [[None for _ in range(m+1)] for _ in range(n+1)]
result2 = 0

def LCS_memo(P, Q, n, m, result):
    if arr[n][m] != None:
        return arr[n][m]
    if n < 0 or m < 0:
        return 0
    if P[n] == Q[m]:
        result = 1 + LCS(P,Q,n-1,m-1,result)
    elif P[n] != Q[n]:
        tmp1 = LCS(P,Q,n-1,m,result)
        tmp2 = LCS(P,Q,n,m-1,result)
        result = max(tmp1, tmp2)
    arr[n][m] = result
    return result

print(LCS_memo(P,Q,n,m,result2))




