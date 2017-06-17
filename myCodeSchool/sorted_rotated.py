import sys

A = [11,12,15,18,19,20,21,2,5,6,8]
# A = [1,2,3,4,5,6]

def linearSearch(A):
    min = sys.maxint
    min_index = 0
    for i in range(len(A)):
        if A[i] < min:
            min = A[i]
            min_index = i

    return min_index

def binarySearch(A):
    low = 0
    n = len(A)
    high = n - 1

    while low <= high:


        if A[low] <= A[high]:
            return low

        mid = (high + low) / 2
        next = (mid + 1) % n
        prev = (mid + n - 1) % n
        if A[mid] <= A[next] and A[mid] <= A[prev]:
            return mid

        if A[mid] <= A[high]:
            high = mid - 1

        if A[mid] >= A[low]:
            low = mid + 1

def binarySearchX(A, x):
    low = 0
    high = len(A) - 1

    while low <= high:
        mid = (low + high) / 2
        if A[mid] == x:
            return mid
        if A[mid] <= A[high]:
            if x > A[mid] and x <= A[high]:
                low = mid + 1
            else:
                high = mid - 1
        else:
            if x >= A[low] and x < A[mid]:
                high = mid - 1
            else:
                low = mid + 1

    return -1


# print linearSearch(A)
# print binarySearch(A)
print binarySearchX(A, 29)