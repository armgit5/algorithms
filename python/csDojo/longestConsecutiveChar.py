# https://www.youtube.com/watch?v=qRNB8CV3_LU&index=10&list=PLBZBJbE_rGRVnpitdvpdY9952IsKMDuev

word = "AABCDDBBBEA"

def longestConChar(word):
    max_char = ""
    prev_char = ""
    max_count = 0
    count = 0

    for c in word:
        if c == prev_char:
            count += 1
        else:
            count = 1
        if count > max_count:
            max_char = c
            max_count = count
        prev_char = c

    print({max_char: max_count})


longestConChar(word)