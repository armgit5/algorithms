# https://www.youtube.com/watch?v=GUDLRan2DWM&list=PL2_aWCzGMAwKedT2KfDMB9YA5DgASZb3U&index=2

import random

# arr = [2,7,4,1,5,3]

# compare current element with next min
# O(n^2)
def selectionSort(arr):

    for i in range(0, len(arr) - 1):
        iMin = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[iMin]:
                iMin = j
        tmp = arr[i]
        arr[i] = arr[iMin]
        arr[iMin] = tmp

# selectionSort(arr)
# print(arr)

# compare with next smaller ele
# O(n^2) -> best case is O(n)
def bubbleSort(arr):

    for k in range(0, len(arr)):
        flag = 0

        # k used to not go throught the already sorted end
        for i in range(0, len(arr) - k - 1):
            if arr[i + 1] < arr[i]:
                tmp = arr[i]
                arr[i] = arr[i + 1]
                arr[i + 1] = tmp
                flag = 1

        # if no more to swap if from 0 to k -> then break
        if flag == 0:
            break

# bubbleSort(arr)
# print(arr)

# best case O(n) avg O(n^2)
def insertionSort(arr):

    # partition from 1 to n-1
    for i in range(1, len(arr)):

        selected = arr[i]
        pivot = i

        # check left partition to be sorted
        while (pivot >= 1 and arr[pivot - 1] > selected):
            arr[pivot] = arr[pivot - 1]
            pivot -= 1

        arr[pivot] = selected

# insertionSort(arr)
# print(arr)

arr = [2,4,1,6,8,5,3,7,9,2,5,23,63,23]
def mergeHelper(arr, l, r):
    copy_arr = arr.copy()
    i = l
    k = l
    mid = (l + r) // 2
    j = mid + 1

    while i <= mid and j <= r:
        if copy_arr[i] <= copy_arr[j]:
            arr[k] = copy_arr[i]
            i += 1
            k += 1
        else:
            arr[k] = copy_arr[j]
            j += 1
            k += 1

    while i <= mid:
        arr[k] = copy_arr[i]
        i += 1
        k += 1

    while j <= r:
        arr[k] = copy_arr[j]
        j += 1
        k += 1

# inplace mergesort https://www.youtube.com/watch?v=rZ9lcXCWSUg
# https://www.geeksforgeeks.org/python-program-for-merge-sort/
def mergeSort(arr, l, r):

    if l >= r:
        return

    mid = (l + r) // 2

    mergeSort(arr, l, mid)
    mergeSort(arr, mid + 1, r)
    mergeHelper(arr, l, r)

# mergeSort(arr, 0, len(arr) - 1)
# print(arr)


# select partition index, then quick sort left and right
def swap(arr, start, end):
    tmp = arr[start]
    arr[start] = arr[end]
    arr[end] = tmp

# arr = [2,1,3,4,8,5,7,6]
arr = [2,4,1,6,8,5,3,7,9,2,5,23,63,23]

# https://www.youtube.com/watch?v=WBkJHxjyDLA
# https://www.youtube.com/watch?v=tpKI9_gA3s0
# https://www.geeksforgeeks.org/quicksort-using-random-pivoting/
# def partition(arr, start, end):
#     pivot = arr[start]
#     left = start + 1
#     right = end
#
#     while True:
#         while left <= right and arr[left] <= pivot:
#             left += 1
#         while left <= right and arr[right] >= pivot:
#             right -= 1
#         if (left >= right):
#             break
#         else:
#             swap(arr, left, right)
#     swap(arr, start, right)
#     return right

def partition(arr, start, end):
    pivot = arr[end]
    pIndex = start
    for i in range(start, end):
        if arr[i] <= pivot:
            if pIndex != i:
                swap(arr, i, pIndex)
            pIndex += 1
    swap(arr, end, pIndex)
    return pIndex

def quickSort(arr, start, end):
    if start < end:
        randPivot = random.randrange(start, end + 1)
        arr[randPivot], arr[end] = arr[end], arr[randPivot]

        pIndex = partition(arr, start, end)
        quickSort(arr, start, pIndex - 1)
        quickSort(arr, pIndex + 1, end)


quickSort(arr, 0, len(arr) - 1)
print(arr)
# print(random.randrange(0, 10))