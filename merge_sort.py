

import sys

unsorted = ['31415926535897932384626433832795', '1', '3', '10', '3', '5']

def merge(left, right):
    i = 0
    j = 0
    ret_list = []
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            ret_list.append(left[i])
            i += 1
        else:
            ret_list.append(right[j])
            j += 1
    ret_list += left[i:]
    ret_list += right[j:]

    return ret_list

def msort(a):
    if len(a) < 2:
        return a
    mid = len(a) / 2
    left = msort(a[:mid])
    right = msort(a[mid:])

    return merge(left, right)


def insertionSort(ar):
    key = ar[-1]
    key_pos = len(ar) - 1
    i = len(ar) - 2
    done = False
    while  i >= 0 and done == False:
        print(ar[i], key)
        if ar[i] > key:
            ar[i+1] = ar[i]
            print(' '.join(map(str, ar)))
        elif ar[i] < key:
            ar[i+1] = key
            print(' '.join(map(str, ar)))
            done = True
        if i == 0 and done == False:
            ar[i] = key
            print(' '.join(map(str, ar)))
        i -= 1
# print '\n'.join(map(str, insertionSort(map(int, unsorted))))
ar = list(map(int, unsorted))

print(insertionSort(ar))

