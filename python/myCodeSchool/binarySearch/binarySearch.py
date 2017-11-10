arr = [2,6,13,21,36,47,63,81,97]

def binarySearch(arr, num):

    if arr == None or len(arr) == 0:
        return -1
    start = 0
    end = len(arr)-1

    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == num:
            return mid
        if num < arr[mid]:
            end = mid - 1
        else:
            start = mid + 1

    return -1

print(binarySearch(arr, 81))