# https://leetcode.com/problems/3sum/description/
# https://www.geeksforgeeks.org/find-a-triplet-that-sum-to-a-given-value/
arr = [-1, 0, 1, 2, -1, -4]
arr2 = [-2, 0, 1, 1, 2]
arr3 = [12, 3, 6, 1, 6, 9]

def three_sum_brute_force(arr, sum):
    n = len(arr)
    out = []
    for i in range(n - 2):
        for j in range(i + 1, n - 1):
            for k in range(j + 1, n):
                if (arr[i] + arr[j] + arr[k]) == sum:
                    out.append([arr[i], arr[j], arr[k]])

    print(out)
# three_sum_brute_force(arr, 0)
# three_sum_brute_force(arr3, 24)


# https://www.geeksforgeeks.org/uni
#
# que-triplets-sum-given-value/
def unique_three_sum(arr, sum):
    # sort array
    arr.sort()

    pair = []
    set_map = set([])

    for i in range(len(arr) - 2):
        # index of the second element
        j = i + 1
        # index of the last element
        k = len(arr) - 1

        while j < k:
            if (arr[i] + arr[j] + arr[k]) == sum:
                temp_str = str(arr[i]) + ":" + str(arr[j]) + ":"
                if temp_str not in set_map:
                    pair.append([arr[i], arr[j], arr[k]])
                    set_map.add(temp_str)
                j += 1
                k -= 1
            elif (arr[i] + arr[j] + arr[k]) < sum:
                j += 1
            else:
                k -= 1
    print(pair)

# unique_three_sum(arr, 0)


class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        nums.sort()

        pair = []
        set_map = set([])
        triplets = []

        for i in range(len(nums) - 2):
            # index of the second element
            j = i + 1
            # index of the last element
            k = len(nums) - 1

            while j < k:
                if (nums[i] + nums[j] + nums[k]) == 0:
                    temp_str = str(nums[i]) + ":" + str(nums[j]) + ":"
                    if temp_str not in set_map:
                        pair.append([nums[i], nums[j], nums[k]])
                        set_map.add(temp_str)
                    j += 1
                    k -= 1
                elif (nums[i] + nums[j] + nums[k]) < 0:
                    j += 1
                else:
                    k -= 1

        return pair

s = Solution()
print(s.threeSum(arr))
