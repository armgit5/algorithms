# https://www.geeksforgeeks.org/find-number-pairs-xy-yx/
X = [2,1,6]
Y = [1,5]

import bisect

# Time complexity of m**n
def countPairsBruteForce(x, y):

    output = []

    for i in x:
        for j in y:
            if i ** j > j ** i:
                output.append((i, j))
    print(output)


# Size of x in m and size of y is n
# Time complexity nlogn to sort y
# Search x in y takes mlogn
# Total run time is nlogn + mlogn
def countPairs(X, Y):

    # Store counts of 0-4 in array Y
    NoOfY = [0] * 5
    for i in range(len(Y)):
        if (Y[i] < 5):
            NoOfY[Y[i]] += 1

    # Sort y
    Y.sort()

    # Loop every x and count pairs with Y
    totalPairs = 0
    for i in X:
        totalPairs += count_helper(i, Y, NoOfY)

    print(totalPairs)

# Helper function to count pairs
def count_helper(x, Y, NoOfY):
    # If x is 0 then there is no value in Y
    if x == 0: return 0

    # If x is 1 then numbers of pairs is numbers of zeros in Y
    if x == 1:
        return NoOfY[0]

    # Find numbers of y in Y with values more than x
    idx = bisect.bisect_right(Y, x)
    ans = len(Y) - idx

    # This step x must be > 1
    # add nums 0 and nums 1
    ans += (NoOfY[0] + NoOfY[1])

    # Decrease number of pairs for x = 2 and y = 4 or 3
    if x == 2: ans -= (NoOfY[3] + NoOfY[4])

    # Increase number of pairs for x = 3 and y = 2
    if x == 3: ans += NoOfY[2]

    return ans


countPairsBruteForce(X, Y)
countPairs(X, Y)

X = [10, 19, 18]
Y = [11, 15, 9]

countPairsBruteForce(X, Y)
countPairs(X, Y)

# print([(1,0)] + [(2,0)])
# arr = [1,2,1,2,1,1,3,4,5]
# print(bisect.bisect_right(arr, 3))