# https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/

# S = "())"
# S = "((("
# S = "()"
S = "()))(("

def minAddToMakeValid(S):
    add = 0  # for )
    bal = 0  # for (

    start = '('
    end = ')'
    for c in S:
        if c in start:
            bal += 1
        else:
            bal -= 1

        if bal == -1:
            add += 1
            bal += 1

    print(bal + add)


minAddToMakeValid(S)
