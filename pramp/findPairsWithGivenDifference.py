# https://www.pramp.com/question/XdMZJgZoAnFXqwjJwnpZ
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


def findPairsWithGivenDifferenceBinarySearch(arr, k):
    # your code goes here
    arr.sort()

    def getY(x, k):
        y = x - k
        return y

    result = []

    for x in arr:
        y = getY(x, k)
        if y != x and binarySearch(arr, y):
            result.append([x, y])

    return result


def findPairsWithGivenDifferenceBrute(arr, k):
    # your code goes here
    arr.sort()

    def getY(x, k):
        y = x - k
        return y

    result = []

    for x in arr:
        y = getY(x, k)
        if y != x and y in arr:
            result.append([x, y])

    return result

def findPairsWithGivenDifference(arr, k):
    arr.sort()
    x = 1
    y = 0
    result = []

    while x < len(arr) and y < len(arr):
        if x != y and arr[x] - arr[y] == k:
            result.append([arr[x],arr[y]])
            x += 1
        elif arr[x] - arr[y] < k:
            x += 1
        elif arr[x] - arr[y] > k:
            y += 1
    return result


arr = [0, -1, -2, 2, 1]
k = 1
print findPairsWithGivenDifferenceBrute(arr, k)
print findPairsWithGivenDifferenceBinarySearch(arr, k)
print findPairsWithGivenDifference(arr, k)

