# https://www.pramp.com/question/wqNo9joKG6IJm67B6z34

arr = ['x','y','z']
str = "xyyzyxyx"

def getShortestBruteForce(arr, str):

    result = ""
    countMap = {}
    min = 10000

    # initialize countMap
    def initCountMap():
        countMap = {}
        for i in arr:
            countMap[i] = 0
        return countMap

    countMap = initCountMap()

    for i in range(len(str)):
        for j in range(i, len(str)):
            # count char in array
            if str[j] in countMap:
                countMap[str[j]] += 1
            # if all char have been seen
            if 0 not in list(countMap.values()):
                diff = j - i + 1
                if diff < min:
                    min = diff
                    result = str[i:j+1]
                # if result is new or x,y,z are 1 of each
                if result == "" or diff < len(result):
                    result = str[i:j+1]
                    break
        # reinit countmap
        countMap = initCountMap()
    return result

print(getShortestBruteForce(arr, str))

# def getShortest2(arr, str):
#     headIndex = 0
#     result = ""
#     countMap = {}
#     uniqueCounter = 0
#
#     # initialize map
#     for i in

def getShortestUniqueSubstring(arr, str):
    headIndex = 0
    result = ""
    uniqueCounter = 0
    countMap = {}

    # initialize countMap
    for i in arr:
        countMap[i] = 0

    # scan str
    for tailIndex in range(len(str)):
        # handle the new tail
        tailChar = str[tailIndex]

        # skip all the characters not in arr
        if tailChar not in countMap:
            continue

        tailCount = countMap[tailChar]
        if tailCount == 0:
            uniqueCounter += 1

        countMap[tailChar] += 1

        # push head forward
        while uniqueCounter == len(arr):
            tempLength = tailIndex - headIndex + 1
            if tempLength == len(arr):
                # return a substring of str from
                # headIndex to tailIndex (inclusive)
                return str[headIndex:tailIndex+1]

            if result == "" or tempLength < len(result):
                # return a substring of str from
                # headIndex to tailIndex (inclusive)
                result = str[headIndex:tailIndex+1]

            headChar = str[headIndex]

            if headChar in countMap:
                headCount = countMap[headChar] - 1
                if headCount == 0:
                    uniqueCounter = uniqueCounter - 1
                countMap[headChar] = headCount

            headIndex += 1

    return result

print(getShortestUniqueSubstring(arr, str))