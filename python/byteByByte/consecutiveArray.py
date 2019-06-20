# https://www.youtube.com/watch?v=1t-082mMScY&index=43&list=PLNmW52ef0uwsjnM06LweaYEZr-wjPKBnj
# if by sorting would be o(nlogn) time o(1) space
# [4,2,1,6,5] = [4,5,6]

arr = [4,2,1,6,5,9,10,11,12]

# This method uses hash map
# runtime is o(n) and space is o(n).
def consecutive(arr):
    # Init set map for look up o(n)
    setMap = set()
    for num in arr:
        setMap.add(num)

    m = 0
    outputArr = []
    for num in arr:
        # Check is there is this value - 1
        # then this value has been added in setMap
        # it has been used to calculate for max value
        if num - 1 in setMap:
            continue

        # If the value is not in set map
        # check for next val, then count length to 1
        l = 1

        while num + 1 in setMap:
            l += 1
            outputArr.append(num)
            num += 1

        outputArr.append(num)

        # Check l if more than max, then it will be max
        if l > m:
            m = l
            outputArr
        else:
            outputArr = []


    return (m, outputArr)

print(consecutive(arr)[0], consecutive(arr)[1])


