# https://leetcode.com/problems/number-of-subarrays-with-bounded-maximum/

class Solution(object):
    def numSubarrayBoundedMax(self, A, L, R):
        """
        :type A: List[int]
        :type L: int
        :type R: int
        :rtype: int
        """
        outIndex = inIdex = -1;
        ans = 0
        for i in range(len(A)):
            # between L and R
            if A[i] >= L and A[i] <= R:
                inIdex = i
                ans += i - outIndex
            # more than R
            elif A[i] > R:
                outIndex = i
            # less than L
            elif inIdex > outIndex:
                ans += inIdex - outIndex

        return ans



A = [2, 1, 4, 3]
L = 2
R = 3

s = Solution()
print(s.numSubarrayBoundedMax(A, L, R))