

s = "aaabccddd"

i = 0
while i < len(s) - 1:
    j = i + 1
    if s[i] == s[j]:
        s = s[:i] + s[j + 1:]
        i = max(i - 1, 0)
    else:
        i += 1
if s == "":
    print("Empty String")
else:
    print(s)



