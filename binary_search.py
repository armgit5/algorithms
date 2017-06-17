a = [2,6,13,21,36,47,63,81,97]

def binarySearch(a, x):
    start = 0
    end = len(a) - 1
    while start <= end:
        mid = (start + end) / 2
        if x == a[mid]:
            return True
        if x < a[mid]:
            end = mid - 1
        else:
            start = mid + 1
    return False

print binarySearch(a, 63)