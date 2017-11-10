# https://www.youtube.com/watch?v=bGC2fNALbNU&list=PLBZBJbE_rGRVnpitdvpdY9952IsKMDuev&index=6

arr = [1,2]


def helper(arr, subset, i):
    if i == len(arr):
        print(subset)
    else:
        subset[i] = 0
        helper(arr, subset, i+1)
        subset[i] = arr[i]
        helper(arr, subset, i+1)



def subsets(arr):
    subset = [0] * len(arr)
    helper(arr, subset, 0)


def subsetsIter(arr):
    subset = [[]]
    temp = []
    for num in arr:
        for item in subset:
            temp += [item + [num]]
        subset += temp
    print(temp)

# subsets(arr)
print("")
subsetsIter(arr)