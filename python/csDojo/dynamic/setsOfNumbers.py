# https://www.youtube.com/watch?v=nqlNzOcnCfs&list=PLBZBJbE_rGRU5PrgZ9NBHJwcaZsNpf8yD&index=4

arr = [2,4,6,10]

def count_sets(arr, total):
    return rec(arr, total, len(arr)-1)

def count_sets_dp(arr, total):
    mem =  {}
    return dp(arr, total, len(arr)-1, mem)

def rec(arr, total, i):
    if total == 0:
        return 1
    if total < 0:
        return 0
    if i < 0:
        return 0
    if total < arr[i]:
        return rec(arr, total, i-1)
    else:
        return rec(arr, total-arr[i], i-1) + rec(arr, total, i-1)

def dp(arr, total, i, mem):
    key = str(total) + ':' + str(i)
    if key in mem:
        return mem[key]

    if total == 0:
        return 1
    if total < 0:
        return 0
    if i < 0:
        return 0
    if total < arr[i]:
        to_return = rec(arr, total, i-1)
    else:
        to_return = rec(arr, total-arr[i], i-1) + rec(arr, total, i-1)

    return to_return


print(count_sets(arr, 16))
print(count_sets_dp(arr, 16))

