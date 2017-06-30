
arr = [ 'p', 'e', 'r', 'f', 'e', 'c', 't', '  ',
                'm', 'a', 'k', 'e', 's', '  ',
                'p', 'r', 'a', 'c', 't', 'i', 'c', 'e' ]

def reverseWords_stack(arr):
    # your code goes here
    stack = []
    temp_w = []
    output = []

    for c in arr:
        if c != '  ':
            temp_w.append(c)
        if c == '  ':
            stack.append(temp_w)
            temp_w = []

    stack.append(temp_w)

    for _ in range(len(stack)):
        word = stack.pop()

        for c in word:
            output.append(c)
        output.append(' ')

    print(output)

def reverseWords(arr):

    mirrorReverse(arr, 0, len(arr)-1)
    wordStart = None

    for i in range(len(arr)):
        if arr[i] == '  ':
            if wordStart != None:
                mirrorReverse(arr, wordStart, i-1)
                wordStart = None
        elif i == len(arr)-1:
            if wordStart != None:
                mirrorReverse(arr, wordStart, i)
        else:
            if wordStart == None:
                wordStart = i


def mirrorReverse(arr, start, end):
    while start < end:
        tmp = arr[start]
        arr[start] = arr[end]
        arr[end] = tmp
        start += 1
        end -= 1

reverseWords_stack(arr)
reverseWords(arr)
print(arr)

