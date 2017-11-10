# https://leetcode.com/problems/two-sum/#/description

nums = [2, 7, 11, 15]
target = 9

class Solution:
    def twoSum(self, nums, target):
        lookup = {}

        for i, val in enumerate(nums):
            diff = target - val
            if diff in lookup:
                return [lookup[diff], i]
            lookup[val] = i

s = Solution()
print(s.twoSum(nums, target))