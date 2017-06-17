

n = 8
# s = "bccbbbbc"

s = "bccbbbbc"

def palindromic_substrings(text):
    results = set()
    text_length = len(text)
    unique_cha = []
    for idx, char in enumerate(text):
        if char not in unique_cha:
            unique_cha.append(char)
        # Check for longest odd palindrome(s)
        start, end = idx - 1, idx + 1

        while start >= 0 and end < text_length and text[start] == text[end]:

            results.add(text[start:end+1])
            start -= 1
            end += 1

        # Check for longest even palindrome(s)
        start, end = idx, idx + 1
        while start >= 0 and end < text_length and text[start] == text[end]:
            results.add(text[start:end+1])
            start -= 1
            end += 1

    return unique_cha + list(results)

def iterate_char(s):
    result = []
    for i in range(1, len(s)):
        result.append(s[:i])
    return result

def propertyOfString(s):
    # Complete this function
    prev = []
    for i in range(1, len(s) + 1):
        substring =  s[:i]

        palindrome = palindromic_substrings(substring)

        result = palindrome
        print palindrome
        for p in palindrome:
            for i in range(1, len(p) + 1):
                subp = p[:i]
                if subp not in result:
                    result.append(subp)

        print len(result)


propertyOfString(s)