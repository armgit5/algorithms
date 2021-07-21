# https://leetcode.com/problems/maximum-repeating-substring/
class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        cnt = 0
        tempWord = word
        # in 32ms faster in find 60ms
        # https://stackoverflow.com/questions/18437798/find-vs-in-operation-in-string-python
        while tempWord in sequence:
        # while sequence.find(tempWord) > -1:
            # print(tempWord)
            cnt += 1
            tempWord += word
        return cnt


sequence = "aaabaaaabaaabaaaabaaaabaaaabaaaaba"
"aaaba"
word = "aaaba"
# sequence = "ababc"
# word = "ab"

s = Solution()
print(s.maxRepeating(sequence, word))

# sequence = "ababc"
# word = "ba"
# s = Solution()
# print(s.maxRepeating(sequence, word))
#
# sequence = "ababc"
# word = "ac"
# s = Solution()
# print(s.maxRepeating(sequence, word))