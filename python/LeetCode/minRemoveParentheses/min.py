# https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/
# https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/discuss/1280611/Simple-and-easy-c%2B%2B-code-with-one-stack-pair

class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        ans = [""] * len(s)
        for i in range(len(s)):
            if s[i] == '(': # keep track of ( index but don't add ( yet
                stack.append(i)
                continue
            if s[i] == ')':
                if stack: # add ) when there is stack
                    ans[i] = ')'
                    beforeI = stack.pop()
                    ans[beforeI] = '(' # valid bracket
                continue
            ans[i] = s[i]

        return "".join(ans)



s = "lee(t(c)o)de)"
sol = Solution()
print(sol.minRemoveToMakeValid(s))

s = "a)b(c)d"
sol = Solution()
print(sol.minRemoveToMakeValid(s))

s = "))(("
sol = Solution()
print(sol.minRemoveToMakeValid(s))

s = "(a(b(c)d)"
sol = Solution()
print(sol.minRemoveToMakeValid(s))

