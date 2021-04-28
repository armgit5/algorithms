

s = "}][}}(}][))]"
s2 = "[](){()}"
s3 = "({}([][]))[]()"
s4 = "{)[](}]}]}))}(())("

def isBalanced(s):
    start = "{[("
    end = "}])"

    stack = []

    # Loop through s
    for c in s:
        if c in start:
            stack.append(c)
        if c in end:
            # Check if starting is end brancket
            if len(stack) == 0:
                return False

            startIndex = start.index(stack.pop())
            endIndex = end.index(c)

            if startIndex != endIndex:
                return False

    if len(stack) == 0:
        return True
    else:
        return False

print(isBalanced(s))
print(isBalanced(s2))
print(isBalanced(s3))
print(isBalanced(s4))