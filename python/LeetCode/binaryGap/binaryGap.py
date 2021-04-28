# https://leetcode.com/problems/binary-gap/
# https://www.geeksforgeeks.org/python-program-to-covert-decimal-to-binary-number/

class Solution(object):
    def __init__(self):
        self.arr = []

    def binaryGap(self, N):
        """
        :type N: int
        :rtype: int
        """
        # if N > 1:
        #     self.binaryGap(N // 2)
        # self.arr.append(N % 2)
        ans = 0
        last = None

        # shift right until ends
        for i in range(32):
            # check if last digit is 1
            if N >> i & 1:
                if last is not None:
                    ans = max(ans, i - last)
                last = i

        return ans

s = Solution()
one = s.binaryGap(33556480) #10110 = 2
print(one)

# print (22 >> 1 & 1) # shift right last result is 1

# two = s.binaryGap(5) #101 = 1 -> 2
# print(two)
#
# three = s.binaryGap(6) # 110 = 1 -> 1
# print(three)
#
# four = s.binaryGap(8) # 1000 = 0 -> 0
# print(four)