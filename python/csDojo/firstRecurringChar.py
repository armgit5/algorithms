
char = "abca"
char2 = "bcaba"

def firstRecurringChar(s):
    map = {}
    for i in s:
        if i not in map:
            map[i] = 1
        else:
            print(i)
            break
firstRecurringChar(char)
firstRecurringChar(char2)