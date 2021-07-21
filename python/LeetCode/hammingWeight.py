# https://leetcode.com/problems/number-of-1-bits/solution/

class Solution:
    # flip n & (n-1) until 0
    def hammingWeight(self, n: int) -> int:
        sum = 0

        while n != 0:
            sum += 1
            n &= n-1

        return sum
s = Solution()

n = 11
print(s.hammingWeight(n))


# print("{0:b}".format(11))
# print(n & 1)
#
# mask = 1
# print(mask, "{0:b}".format(mask))
# mask <<= 1
# print(mask, "{0:b}".format(mask))
# mask <<= 1
# print(mask, "{0:b}".format(mask))
