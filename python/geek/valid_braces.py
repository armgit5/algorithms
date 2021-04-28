
def validBraces(string):
    stack = []
    starting_brackets = "({["
    ending_brackets = ")}]"

    # Loop through all chars in string
    for c in string:

        # If char in starting brackets then add to stack
        if c in starting_brackets:
            stack.append(c)

        # If char in ending brackets then
        # pop from stack and if pop char
        # matches the current char like ')' '('
        # then it's valid if not then not valid
        elif c in ending_brackets:

            last_char = ''
            if len(stack) != 0:
                last_char = stack.pop()

            if c == ')':
                if last_char != '(':
                    return False

            if c == '}':
                if last_char != '{':
                    return False

            if c == ']':
                if last_char != '[':
                    return False

    # Check to make sure stack if empty
    # if not empty then it's not valid
    return len(stack) == 0



test_braces =  "(){c}a[d]";
print(validBraces(test_braces))
print(validBraces( "(}" ))
print(validBraces( "[(ab]cd)" ))
print(validBraces( "([{}])" ))
print(validBraces(")(}{]["))