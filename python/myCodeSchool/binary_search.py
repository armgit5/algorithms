

# A = [2,4,10,10,10,18,20]
A = [1,1,3,3,5,5,5,5,5,9,9,11]

def binarySearch(A, n, x, flag):
    low = 0
    high = n

    result = -1

    while low <= high:
        mid = (low + high) / 2
        if A[mid] == x:
            result = mid
            if flag == 0:
                high = mid - 1
            if flag == 1:
                low = mid + 1

        elif x < A[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return result

def findCount(A, n, x):
    first = binarySearch(A, n, x, 0)
    last = binarySearch(A, n, x, 1)

    return last - first + 1

print((findCount(A, len(A)-1, 5)))


# print binarySearch(A, len(A)-1, 10, 1)

