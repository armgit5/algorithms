# https://leetcode.com/problems/subsets/description/

arr = [1,2,3]
arr2 = [1,2,2]
ans = [
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]

class Solution(object):

    def subsetsIter(self, nums):
        res = [[]]
        for num in sorted(nums):
          res += [item + [num] for item in res]
        return res

    '''
              123 
       1       2      3
     12 13      23
    123 
    '''
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        self.dfs(sorted(nums), 0, [], res)
        return res


    def dfs(self, nums, index, path, res):
        # a = path
        # b = index
        # c = res
        res.append(path)
        for i in range(index, len(nums)):
            if (i > index and nums[i] == nums[i - 1]):
              continue
            self.dfs(nums, i+1, path+[nums[i]], res)

    def subsetsWithDup(self, S):
      res = [[]]
      S.sort()
      for i in range(len(S)):
        if i == 0 or S[i] != S[i - 1]:
          l = len(res)
        a = len(res) - l
        b = len(res)
        for j in range(len(res) - l, len(res)):
          res.append(res[j] + [S[i]])
      return res

    def subsetsBacktrack(self, nums):
      l = []
      self.backtrack(l, [], sorted(nums), 0)
      return l

    def backtrack(self, l, tempList, nums, start):
      l.append(tempList)
      for i in range(start, len(nums)):
        if (i > start and nums[i] == nums[i-1]):
          continue
        self.backtrack(l, tempList + [nums[i]], nums, i+1)
        # tempList.pop(len(tempList)-1)


# print(arr)
s = Solution()
print(s.subsets(arr))
print(s.subsetsIter(arr))
print(s.subsetsWithDup(arr))
print(s.subsetsBacktrack(arr))
print("")
print(s.subsets(arr2))
print(s.subsetsIter(arr2))
print(s.subsetsWithDup(arr2))
print(s.subsetsBacktrack(arr2))