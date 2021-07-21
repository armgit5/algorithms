# https://leetcode.com/problems/subarray-sums-divisible-by-k/
# https://circlecoder.com/subarray-sum-divisible-by-k/
# https://leetcode.com/problems/subarray-sums-divisible-by-k/discuss/1201799/Python-easy-solution
# subarray between these two accu_sum has a sum divisible by k.
from typing import List, Set, Tuple, Dict
import collections

class Solution:
    def subarraysDivByK(self, A: List[int], K: int) -> int:
        rem_map = collections.defaultdict(int)
        rem_map[0] = 1
        sum, ans = 0, 0
        for n in A:
            sum += n
            rem = sum % K
            ans += rem_map[rem]
            rem_map[rem] += 1
        return ans


nums = [4,5,0,-2,-3,1]
k = 5

s = Solution()
ans = s.subarraysDivByK(nums, k)
print(ans)