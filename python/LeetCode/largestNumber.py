# https://leetcode.com/problems/largest-number/

# Not working
def largestNumberOld(nums):

    strOut = ''
    while len(nums) > 0:
        max = nums[0]
        maxIndex = 0
        for i in range(1, len(nums)): # num element
            strNum = str(nums[i])
            for j in range(len(strNum)): # char in num
                intNum = int(strNum[j])
                strMax = str(max)
                for k in range(len(strMax)):
                    intMax = int(strMax[k])
                    if intNum < intMax:
                        break
                    elif intNum == intMax:
                        continue
                    else:
                        max = nums[i]
                        maxIndex = i
                        break
                break

        nums.pop(maxIndex)
        strOut += str(max)
    print(strOut)

# Use sort comparator
# https://www.geeksforgeeks.org/given-an-array-of-numbers-arrange-the-numbers-to-form-the-biggest-number/
# https://leetcode.com/problems/largest-number/solution/

# Quick sort
# https://leetcode.com/problems/largest-number/discuss/518018/Python-Memory-less-than-100.0-and-faster-than-67.66
# https://leetcode.com/problems/largest-number/discuss/513929/Python3-solution-with-quick-sort.-Faster-than-46.49

class Compare(str):
    def __lt__(x, y):
        return x + y > y + x

# def compare(x, y):
#     return x + y > y + x

def largestNumber(nums):
    strNums = list(map(lambda x : str(x), nums))
    sortedStrNums = sorted(strNums, key=Compare)
    outStr = ''.join(sortedStrNums)
    print(outStr)



input = [3,30,34,5,9]
input2 = [30,34,5,9,3]
input3 = [20,1]
input4 = [0,0]

largestNumber(input)
largestNumber(input2)
largestNumber(input3)
largestNumber(input4)
