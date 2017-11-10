# https://www.hackerrank.com/challenges/marcs-cakewalk

a =  [1,3,2]

def cakeWalk(a):
    a.sort()
    a.reverse()
    minMile = 0

    for i in range(len(a)):
        minMile += a[i]*2**i
        print(minMile)
    return minMile

print((cakeWalk(a)))
