# https://www.youtube.com/watch?v=XMKMgzU1uiw&list=PLNmW52ef0uwsjnM06LweaYEZr-wjPKBnj&index=8

s = "aaabcccc"

def stringCompress(s):
    out = ""
    sum = 1

    for i in range(len(s) - 1):
        if s[i] == s[i + 1]:
            sum += 1
        else:
            # append previous char if next char not the same
            out = out + s[i] + str(sum)
            sum = 1

    # Append remaining chars or char
    out = out + s[len(s)-1] + str(sum)

    return s if len(s) == 1 else out

print(stringCompress(s))
