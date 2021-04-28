input = [2,3,1,1,4] # 2
# input = [1] # 0
input4 = [8,2,4,4,4,9,5,2,5,8,8,0,8,6,9,1,1,6,3,5,1,2,6,6,0,4,8,6,0,3,2,8,7,6,5,1,7,0,3,4,8,3,5,9,0,4,0,1,0,5,9,2,0,7,0,2,1,0,8,2,5,1,2,3,9,7,4,7,0,0,1,8,5,6,7,5,1,9,9,3,5,0,7,5]
input2 = [1,2,1,1,1]
input3 = [1,4,3,7,1,2,6,7,6,10]

def jumpDFS(nums):

    if len(nums) <= 1:
        return 0

    endIndex = len(nums) - 1

    q = []
    q.append((0, nums[0], 0))
    while len(q) > 0:
        i, n, cnt = q.pop(0)
        cnt += 1
        # travel n steps
        for j in range(i + n, i, -1):
            if j < endIndex:
                q.append((j, nums[j], cnt))
            else:
                return cnt


    return 0

print(jumpDFS(input))
print(jumpDFS(input2))
print(jumpDFS(input3))

# https://www.youtube.com/watch?v=vBdo7wtwlXs
# https://leetcode.com/problems/jump-game-ii/discuss/517077/C-solution(Greedy-93-fast)
# https://leetcode.com/problems/jump-game-ii/discuss/520101/python-greedy-solution


def jump(nums):

    if len(nums) <= 1:
        return 0

    ladderMax = nums[0]
    currentMax = nums[0] # where you stay before jumping to new ladder
    jump = 1

    for i in range(1, len(nums)):
        if i > currentMax:
            jump += 1
            currentMax = ladderMax

        if i + nums[i] > ladderMax:
            ladderMax = i + nums[i]

    print(jump)
print('new')
jump(input)
jump(input2)
jump(input3)
jump(input4)





