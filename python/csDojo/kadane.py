# https://www.youtube.com/watch?v=86CQq3pKSUw

arr = [-2,3,2,-1]



def max_subarray(arr):
    max_current, max_global = arr[0], arr[0]
    for i in range(1, len(arr)):
        max_current = max(arr[i], max_current + arr[i])
        max_global = max(max_current, max_global)
    return max_global

print(max_subarray(arr))