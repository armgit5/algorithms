# https://leetcode.com/problems/minimum-elements-to-add-to-form-a-given-sum/
# https://leetcode.com/problems/minimum-elements-to-add-to-form-a-given-sum/discuss/1136869/Extremely-short-and-Simplest-Java-solution
import math
class Solution(object):
    def minElements(self, nums, limit, goal):
        """
        :type nums: List[int]
        :type limit: int
        :type goal: int
        :rtype: int
        """

        sum = 0
        for n in nums:
            sum += n

        if sum == goal:
            return 0
        else:
            # it takes math.ceil(abs(goal)/ limit) steps to reach goal
            return math.ceil(abs(goal - sum)/ limit)


# nums = [1,-1,1]
# limit = 3
# goal = -4
# s = Solution()
# print(s.minElements(nums, limit, goal))
# assert s.minElements(nums, limit, goal) == 2
#
#
# nums = [1,-10,9,1]
# limit = 100
# goal = 0
# s = Solution()
# print(s.minElements(nums, limit, goal))
# assert s.minElements(nums, limit, goal) == 1


nums = [1,-7,-5,9,0,14]
limit = 14
goal = 14
s = Solution()
print(s.minElements(nums, limit, goal))
# assert s.minElements(nums, limit, goal) == 1

# print(abs(goal - 1)/ limit)
# print(math.ceil(abs(goal - 1)/ limit))
