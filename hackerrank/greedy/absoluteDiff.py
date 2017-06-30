# https://www.hackerrank.com/challenges/minimum-absolute-difference-in-an-array

import sys

n = 3
a = [3, -7, 0]




def abMinBrute(n, a):
    min = sys.maxsize
    for i in range(len(a)-1):
        for j in range(i+1, len(a)):
            diff = abs(a[i]-a[j])
            if diff < min:
                min = diff
    return min

def abMin(n, a):
    sortedA = sorted(a)
    min = sys.maxsize
    for i in range(n-1):
        diff = abs(sortedA[i]-sortedA[i+1])
        if diff < min:
            min = diff
    return min


print(abMinBrute(n, a))
print(abMin(n, a))


