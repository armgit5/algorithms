# https://www.youtube.com/watch?v=xOlhR_2QCXY&index=2&list=PLBZBJbE_rGRU5PrgZ9NBHJwcaZsNpf8yD

weight = [1,2,4,2,5]
value = [5,3,5,3,2]

n = len(weight)
C = 10

arr = [[None for _ in range(C+1)] for _ in range(n)]
print(arr[4][9])

def KS(n,C):
    if n < 0 or C <= 0:
        result = 0
    elif weight[n] > C:
        result = KS(n-1, C)
    else:
        no = KS(n-1, C)
        yes = value[n] + KS(n-1, C-weight[n])
        result = max(yes, no)
    return result

def KS_memo(n,C):
    if arr[n][C] != None:
        return arr[n][C]
    if n < 0 or C <= 0:
        result = 0
    elif weight[n] > C:
        result = KS(n-1, C)
    else:
        no = KS(n-1, C)
        yes = value[n] + KS(n-1, C-weight[n])
        result = max(yes, no)
    arr[n][C] = result
    return result

print(KS(n-1, C))
print(KS_memo(n-1, C))