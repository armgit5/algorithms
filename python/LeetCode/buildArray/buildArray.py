# https://leetcode.com/problems/build-an-array-with-stack-operations/
# https://leetcode.com/problems/build-an-array-with-stack-operations/discuss/1315003/C%2B%2B-fast-and-understandable-solution-O(n)-time-complexity-and-O(1)-Space-Complexity

from typing import List

class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        res = []
        cnt = 0
        for i in range(1, n+1):
            res.append('Push')
            if i == target[cnt]:
                cnt += 1
                if cnt >= len(target):
                    break
            else:
                res.append("Pop")
        return res


s = Solution()

target = [1,3]
n = 3
print(s.buildArray(target, n))

target = [2,3,4]
n = 4
print(s.buildArray(target, n))

target = [1,2]
n = 4
print(s.buildArray(target, n))