# https://codility.com/c/run/E7SCRN-S7P

K = 12
L = 21

def solutionOOfN(M, N):
    # write your code in Python 2.7

    # sum the first 2 numbers first
    # make the first some as carry
    # to be recalculated next by interating
    # through the loop staring from M+2 index
    startBin = toBin(M)
    nextBin = toBin(M+1)
    startBin, nextBin = makeEqualLength(startBin, nextBin)
    carry = bitxor(startBin, nextBin)

    # used to convert carry to string
    # then can convert string to number from
    # int(string, 2)
    bitorString = ""

    # computer bitxor
    # for i in range(M+2, N+1):
    #     next = toBin(i)
    #     carry, next = makeEqualLength(carry, next)
    #     carry = bitxor(carry, next)

    for i in carry:
        bitorString += str(i)

    # return binary string to integer
    return (int(bitorString,2))

# convert number to binary array
def toBin(num):
    binary = []
    while num != 0:
        bit = num % 2
        binary.insert(0, bit)
        num = int(num // 2)
    return binary

# make the 2 arrays equal length
# by adding 0 in front
def makeEqualLength(arr1, arr2):
    if len(arr2) > len(arr1):
        diff = len(arr2) - len(arr1)
        arr1 = [0] * diff + arr1
    else:
        diff = len(arr1) - len(arr2)
        arr2 = [0] * diff + arr2
    return arr1, arr2

# compute bitxor from 2 binary arrays
def bitxor(arr1, arr2):
    n = len(arr1)
    bitxorArr = []
    for i in range(n):
        if arr1[i] != arr2[i]:
            bitxorArr.append(1)
        else:
            bitxorArr.append(0)
    return bitxorArr



# arr = [5,6,7,8]

# this solution uses O(log(N))
# by splitting the problem in half
def solution(M, N):
    arr = []
    for i in range(M, N+1):
        arr.append(i)

    return splitSum(arr)

# split the arr in half
# then sum sub arrays using bitxor
def splitSum(arr):
    mid = int(len(arr) // 2)
    if len(arr) <= 1:
        return arr[0]
    left = splitSum(arr[:mid])
    right = splitSum(arr[mid:])
    leftBin, rightBin = makeEqualLength(toBin(left), toBin(right))
    sumArray = bitxor(leftBin, rightBin)
    sumString = ""
    for i in sumArray:
        sumString += str(i)
    sumInt = (int(sumString,2))
    return sumInt

print(solution(5,8))