

s = "abc"

def toString(array):
    print(''.join(array))

def permute(array, left, right):

    if left == right:
        toString(array)
    else:
        for i in range(left, right + 1):
            array[left], array[i] = array[i], array[left]
            permute(array, left + 1, right)
            array[left], array[i] = array[i], array[left]


# array = list(s)
# permute(array, 0, len(s) - 1)

# https://leetcode.com/problems/permutations/description/

output = []

class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.output = []
        return self.permuteIntArray(nums, 0, len(nums) - 1)

    def permuteIntArray(self, array, left, right):

        if left == right:
            self.output.append(list(array))
        else:
            for i in range(left, right + 1):
                array[left], array[i] = array[i], array[left]
                self.permuteIntArray(array, left + 1, right)
                array[left], array[i] = array[i], array[left]

        return self.output

s = Solution()
print(s.permute([1,2,3]))
