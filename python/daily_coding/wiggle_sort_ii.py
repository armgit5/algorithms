# https://leetcode.com/problems/wiggle-sort-ii/
# https://www.geeksforgeeks.org/sort-array-wave-form-2/
# https://evelynn.gitbooks.io/google-interview/wiggle_sort_ii.html
# https://leetcode.com/problems/wiggle-sort-ii/discuss/77684/summary-of-the-various-solutions-to-wiggle-sort-for-your-reference/81858


import heapq as hq

# nums1 = [1, 5, 2, 1, 6, 4]
# nums = [1,2,2,1,2,1,1,1,1,2,2,2]
nums = [4,5,5,6] # [5,6,4,5]
nums1 = [1,5,1,1,6,4]

def swap_helper(nums, start, end):
    tmp = nums[start]
    nums[start] = nums[end]
    nums[end] = tmp

def partition(arr, start, end):
    pivot = arr[end]
    pIndex = start
    for i in range(start, end):
        if arr[i] <= pivot:
            if pIndex != i:
                swap_helper(arr, i, pIndex)
            pIndex += 1
    swap_helper(arr, end, pIndex)
    return pIndex

# https://algorithmsandme.com/find-kth-smallest-element-in-array/
# https://www.geeksforgeeks.org/kth-smallestlargest-element-unsorted-array/
# https://www.youtube.com/watch?v=FrWq2rznPLQ
# https://leetcode.com/problems/kth-largest-element-in-an-array/description/
# https://leetcode.com/problems/kth-smallest-element-in-a-bst/
arr = [3,2,1,5,6,4]
arr2 = [3,2,3,1,2,4,5,5,6]
def kLargestElement(arr, k):
    minHeap = []
    for i in arr:
        hq.heappush(minHeap, i)
        if len(minHeap) > k:
            hq.heappop(minHeap)

    return hq.heappop(minHeap)


def partition(arr, start, end):
    pivot = arr[end]
    pIndex = start
    for i in range(start, end):
        if arr[i] <= pivot:
            if pIndex != i:
                arr[i], arr[pIndex] = arr[pIndex], arr[i]
            pIndex += 1
    arr[end], arr[pIndex] = arr[pIndex], arr[end]
    return pIndex

def kLargestQuickSort(arr, k):
    low = 0
    hi = len(arr) - 1

    while low < hi:
        j = partition(arr, low, hi)
        if j < k:
            low = j + 1
        elif j > k:
            hi = j - 1
        else:
            break
    return arr[j]

def kSmallestElemen(arr, k):
    return kLargestElement(arr, len(arr) - k + 1)

# print(kLargestElement(arr, 2))
# print(kSmallestElemen(arr, 1))
# print(kLargestElement(arr2, 4))
# print(5 >> 1) = 5 // 2

arr = [6,13,5,4,5,5,5,2]

def mapIndex(i, n):
    return (1 + 2 * i) % (n | 1)

# https://leetcode.com/problems/wiggle-sort-ii/discuss/77677/ono1-after-median-virtual-indexing
# https://leetcode.com/problems/wiggle-sort-ii/discuss/77682/step-by-step-explanation-of-index-mapping-in-java
def wiggleSortInSpace(arr):
    median = kLargestQuickSort(arr, len(arr) // 2)
    # num = S M L

    n = len(arr)
    left = 0
    right = n - 1
    i = 0

    # print(arr, median)

    while i <= right:

        newIndex = mapIndex(i, n)
        newLeft = mapIndex(left, n)
        newRight = mapIndex(right, n)

        # swap 1 3 5 with large
        # swap 0 2 4 with small
        if  arr[newIndex] > median:
            swap_helper(arr, newIndex, newLeft)
            i += 1
            left += 1
        elif arr[newIndex] < median:
            swap_helper(arr, newIndex, newRight)
            right -= 1
        else:
            i += 1

wiggleSortInSpace(arr)
print(arr)





# median = partition(arr, start)
# wiggleSortInSpace(arr)


# Index :       0   1   2   3   4   5
# Small half:   M       S       S
# Large half:       L       L       M

# def wiggleSortSort(nums):
#     copy_arr = sorted(nums, reverse=True)
#     n = len(nums)
#     m = n // 2
#
#     # odd
#     # i = 1,3,5. j = 0,1,2
#     for i, j in zip(range(1, n, 2), range(0, m)):
#         nums[i] = copy_arr[j]
#
#     # even
#     for i, j in zip(range(0, n, 2), range(m, n)):
#         nums[i] = copy_arr[j]
#
#     print(nums)
#
# wiggleSortSort(nums1)
#
# def wiggleSort1(nums):
#
#     if len(nums) < 2:
#         return nums
#
#     N = len(nums)
#
#     for i in range(1, N, 2):
#         # traverse even ele if current is < left -> swap
#         # if < right -> swap
#         curr = nums[i]
#         left = nums[i - 1]
#         if curr < left:
#             swap_helper(nums, i, i - 1)
#
#         if i != N - 1:
#             right = nums[i + 1]
#             if curr < right:
#                 swap_helper(nums, i + 1, i)
#
#
#
#             pivot = i + 2
#             while curr == right:
#                 right = nums[pivot]
#                 if curr < right:
#                     swap_helper(nums, pivot, i)
#                     break
#                 pivot += 1
#
#     return nums
#
# def wiggleSort2(nums):
#     if not nums:
#         return
#     nums.sort()
#
#     L = len(nums)
#     boundary = L // 2 if L % 2 == 0 else L // 2 + 1
#     small_nums = nums[:boundary]
#     large_nums = nums[boundary:]
#     small_nums, large_nums = small_nums[::-1], large_nums[::-1]
#
#     j, k = 0, 0
#     for i in range(L):
#         if i % 2 == 0:
#             nums[i] = small_nums[j]
#             j += 1
#         else:
#             nums[i] = large_nums[k]
#             k += 1
#     return nums
#
# print(wiggleSort1(nums))
# print(wiggleSort2(nums))
# print(wiggleSort2(nums1))

