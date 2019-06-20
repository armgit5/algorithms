import sys
# Permutation
# https://www.youtube.com/watch?v=IPWmrjE1_MU&t=305s
# https://www.geeksforgeeks.org/write-a-c-program-to-print-all-permutations-of-a-given-string/


# Combination
# https://www.geeksforgeeks.org/print-all-possible-combinations-of-r-elements-in-a-given-array-of-size-n/
# https://www.youtube.com/watch?v=xTNFs5KRV_g&t=404s

arr = [1,2,3]

def permutation(arr, l, r):

    # Base case
    if l == r:
        print(arr)

    # Loop all possible solutions from l to r
    for i in range(l, r+1):
        # Swap l with i
        arr[i], arr[l] = arr[l], arr[i]
        permutation(arr, l+1, r)
        # Back track
        arr[i], arr[l] = arr[l], arr[i]

# permutation(arr, 0 , len(arr)-1)


# # https://www.geeksforgeeks.org/lexicographically-smallest-array-k-consecutive-swaps/
# arr2 = [7, 6, 9, 2, 1]
# smallest = [9, 9, 9, 9, 9]
#
#
#
# def smallestAfterK(arr2, l, r, k, swap):
#     global smallest
#
#     # Base case
#     if l == r and swap == 3:
#         print(arr2, swap)
#     # Loop all possible solutions from l to r
#     for i in range(l, r+1):
#         # Swap l with i
#         arr2[i], arr2[l] = arr2[l], arr2[i]
#         swap += 1
#
#         smallestAfterK(arr2, l+1, r, 3, swap)
#
#         # if arr2 < smallest:
#         #     smallest = arr2
#         #     print(smallest)
#
#         # Back track
#         arr2[i], arr2[l] = arr2[l], arr2[i]
#         swap -= 1
#
#     # print(smallest)
#
#
# smallestAfterK(arr2, 0, len(arr2)-1, 3, 0)
# print(smallest)