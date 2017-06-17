str = "[](){}<>"
str = "(h[e{|<|>o}!]~)()()()("

def hasBalancedBrackets(str):
    # WRITE YOUR CODE HERE

    stack = []

    open_brackets = "<({["
    close_brackets = ">)}]"
    for c in str:
        # Check to see if character in open brackets
        if c in open_brackets:
            stack.append(c)
        # Check to see if character in close brackets
        if c in close_brackets:
            # no open bracket, return 0

            if len(stack) == 0:
                return 0
            else:
                indexOfOpenBracket = open_brackets.index(stack.pop())
                indexOfCloseBracket = close_brackets.index(c)
                if indexOfOpenBracket != indexOfCloseBracket:
                    return 0
    # If stack is empty, that means the bracket is balance
    if len(stack) == 0:
        return 1
    else:
        return 0


print hasBalancedBrackets(str)
