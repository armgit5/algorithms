# https://leetcode.com/problems/remove-palindromic-subsequences/

class Solution(object):
    def removePalindromeSub(self, s):
        """
        :type s: str
        :rtype: int
        """

        if len(s) == 0:
            return 0

        if s == s[::-1]:
            return 1

        return 2


s = "ababa"
sol = Solution()
print(sol.removePalindromeSub(s))
# print(s[::-1])